# %%

from collections import defaultdict
from math import log, sqrt
import re
import numpy as np
import sys
from copy import deepcopy   #   https://docs.python.org/3/library/copy.html

# %%

# ## Import the data ad create the inverted index

def import_dataset():
    """
    This function import all the articles in the TIME corpus,
    returning list of lists where each sub-list contains all the
    terms present in the document as a string.
    """
    articles = []
    with open('TIME.ALL', 'r') as f:
        tmp = []
        for row in f:
            if row.startswith("*TEXT"):
                if tmp != []:
                    articles.append(tmp)
                tmp = []
            else:
                row = re.sub(r'[^a-zA-Z\s]+', '', row)
                tmp += row.split()
    return articles


def remove_stop_words(corpus):
   '''
   This function removes from the corpus all the stop words present in the file TIME.STP
   '''
   stop_w = [line.rstrip('\n') for line in open('TIME.STP')]
   stop_w=list(filter(None, stop_w))
   for i in range(0,len(corpus)):
       corpus[i] = [x for x in corpus[i] if x not in stop_w]
   return corpus 


def make_inverted_index(corpus):
    """
    This function builds an inverted index as an hash table (dictionary)
    where the keys are the terms and the values are ordered lists of
    docIDs containing the term.
    """
    corpus = remove_stop_words(corpus)
    index = defaultdict(set)
    for docid, article in enumerate(corpus):
        for term in article:
            index[term].add(docid)
    return index


# ### Union of two posting lists

def posting_lists_union(pl1, pl2):
        """
        Returns a new posting list resulting from the union of the
        two lists passed as arguments.
        """
        pl1 = sorted(list(pl1))
        pl2 = sorted(list(pl2))
        union = []
        i = 0
        j = 0
        while (i < len(pl1) and j < len(pl2)):
            if (pl1[i] == pl2[j]):
                union.append(pl1[i])
                i += 1
                j += 1
            elif (pl1[i] < pl2[j]):
                union.append(pl1[i])
                i += 1
            else:
                union.append(pl2[j])
                j += 1
        for k in range(i, len(pl1)):
            union.append(pl1[k])
        for k in range(j, len(pl2)):
            union.append(pl2[k])
        return union


# ## Precomputing weights

def DF(term, index):
    '''
    Function computing Document Frequency for a term.
    '''
    return len(index[term])


def IDF(term, index, corpus):
    '''
    Function computing Inverse Document Frequency for a term.
    '''
    return log(len(corpus)/DF(term, index))


def RSV_weights(corpus,index):
    '''
    This function precomputes the Retrieval Status Value weights
    for each term in the index
    '''
    N = len(corpus)
    w = {}
    for term in index.keys():
        p = DF(term, index)/(N+0.5)  
        w[term] = IDF(term, index, corpus) + log(p/(1-p))
    return w
    


# ## BIM Class

class BIM():
    '''
    Binary Independence Model class
    '''
    
    def __init__(self, corpus):
        self.original_corpus = deepcopy(corpus)
        self.articles = corpus
        self.index = make_inverted_index(self.articles)
        self.weights = RSV_weights(self.articles, self.index)
        self.ranked = []
        self.query_text = ''
        self.N_retrieved = 0
    
    
        
    def RSV_doc_query(self, doc_id, query):
        '''
        This function computes the Retrieval Status Value for a given couple document - query
        using the precomputed weights
        '''
        score = 0
        doc = self.articles[doc_id]
        for term in doc:
            if term in query:
                score += self.weights[term]     
        return score

    
        
    def ranking(self, query):
        '''
        Auxiliary function for the function answer_query. Computes the score only for documents
        that are in the posting list of al least one term in the query
        '''

        docs = []
        for term in self.index: 
            if term in query:
                docs = posting_lists_union(docs, self.index[term])
                
        scores = []
        for doc in docs:
            scores.append((doc, self.RSV_doc_query(doc, query)))
        
        self.ranked = sorted(scores, key=lambda x: x[1], reverse = True)
        return self.ranked
    
    
    
    def recompute_weights(self, relevant_idx, query):
        '''
        Auxiliary function for relevance_feedback function and
        for the pseudo relevance feedback in answer_query function.
        Recomputes the weights, only for the terms in the query
        based on a set of relevant documents.
        '''
        
        relevant_docs = []
        for idx in relevant_idx:
            doc_id = self.ranked[idx-1][0]
            relevant_docs.append(self.articles[doc_id])
        
        N = len(self.articles)
        N_rel = len(relevant_idx)
        
        for term in query:
            if term in self.weights.keys():
                vri = 0
                for doc in relevant_docs:
                    if term in doc:
                        vri += 1
                p = (vri + 0.5) /( N_rel + 1)
                u = (DF(term, self.index) - vri + 0.5) / (N - N_rel +1)
                self.weights[term] = log((1-u)/u) + log(p/(1-p))

            
    
    def answer_query(self, query_text):
        '''
        Function to answer a free text query. Shows the first 30 words of the
        15 most relevant documents. 
        Also implements the pseudo relevance feedback with k = 5
        '''
        
        self.query_text = query_text
        query =  query_text.upper().split()
        ranking = self.ranking(query)
        
        ## pseudo relevance feedback 
        i = 0
        new_ranking=[]
        while i<10 and ranking != new_ranking:
            self.recompute_weights([1,2,3,4,5], query)
            new_ranking = self.ranking(query)
            i+=1
        
        ranking = new_ranking
        
        self.N_retrieved = 15
        
        ## print retrieved documents
        
        for i in range(0, self.N_retrieved):
            article = self.original_corpus[ranking[i][0]]
            if (len(article) > 30):
                article = article[0:30]
            text = " ".join(article)
            print(f"Article {i + 1}, score: {ranking[i][1]}")
            print(text, '\n')

        self.weights = RSV_weights(self.articles, self.index)


            
    def relevance_feedback(self, *args):
        '''
        Function that implements relevance feedback for the last query formulated.
        The set of relevant documents is given by the user through a set of indexes
        '''
        if(self.query_text == ''):
            print('Cannot get feedback before a query is formulated.')
            return
        
        relevant_idx = list(args)
        
        if(isinstance(relevant_idx[0], list)):
            relevant_idx = relevant_idx[0]
        
        query = self.query_text.upper().split()
        self.recompute_weights(relevant_idx,query)
        
        self.answer_query(self.query_text)
    
    
    
    def read_document(self,rank_num):
        '''
        Function that allows the user to select a document among the ones returned 
        by answer_query and read the whole text
        '''
        if(self.query_text == ''):
            print('Cannot select a document before a query is formulated.')
            return
            
        article = self.original_corpus[self.ranked[rank_num - 1][0]]
        text = " ".join(article)
        print(f"Article {rank_num}, score: {self.ranked[rank_num][1]}")
        print(text, '\n')
        
        
    def show_more(self):
        '''
        Function that allows the user to see more 10 retrieved documents
        '''
        
        if(self.N_retrieved + 10 > len(self.ranked)):
            print('No more documents available')
            return 
        
        for i in range(self.N_retrieved, self.N_retrieved+10):
            article = self.original_corpus[self.ranked[i][0]]
            if (len(article) > 30):
                article = article[0:30]
            text = " ".join(article)
            print(f"Article {i + 1}, score: {self.ranked[i][1]}")
            print(text, '\n')
        
        self.N_retrieved += 10 
        
# %%

# Example of usage
articles = import_dataset()
bim  = BIM(articles)

# %%
bim.answer_query('Italy and Great Britain fight the enemy')

# %%
bim.relevance_feedback(5,6,8)

# %%
bim.show_more()

# %%
bim.read_document(1)

# %%
# CLASS DECOMPOSITION

## make inverted matrix
make_inverted_index(articles)

# %%
### remove stop words
corpus = remove_stop_words(articles)
corpus

# %%
### create a dictionary with key [term] and value [document id]
index = defaultdict(set)
for docid, article in enumerate(corpus):
    for term in article:
        index[term].add(docid)
index

# %%

# %%