# %%
#   Packages
import spacy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
import string
import re

# %%
class textProcessing(object):
    
    def __init__(self, spacyNLP=spacy.load('en_core_web_sm'), base_form="lemma", pos_filter=None, save_words=[], clean_all=True, stop_words_list=stopwords.words("english"), ngram=1, punctuation=list(string.punctuation)):
        """
        spacyNLP=spacy.load('en_core_web_sm')
        stop_words_list=stopwords.words("english")

        base_form:
            + lemma -> retrieve spaCy lemma
            + porter -> retrieve nltk PorterStemmer
            + snowball -> retrieve nltk SnowballStemmer
            + lancaster -> retrieve nltk LancasterStemmer        
        """
        self.nlp = spacyNLP
        self.base_form = base_form
        self.pos = pos_filter
        self.save_words = save_words
        self.clean_all = clean_all
        self.stop_words_list = stop_words_list
        self.punctuation = punctuation
        self.ngram = ngram
    
    def filteredToken(self, text):
        tokens = []
        if self.stop_words_list!=False:
            if "n't" in self.stop_words_list:
                self.stop_words_list.remove("n't")
            if "not" in self.stop_words_list:
                self.stop_words_list.remove("not")
        else:
            self.stop_words_list = list()
        for token in self.nlp(text):
            tk = token.text.lower()
            tk = re.sub("n't", "not", tk)
            if self.clean_all:
                if (tk not in self.punctuation) and (tk not in self.stop_words_list):
                    if self.base_form=="lemma":
                        tk = token.lemma_
                        if token.lemma_=="n't":
                            tk="not"                                  
                    elif self.base_form=="porter":
                        tk = PorterStemmer().stem(tk)
                    elif self.base_form=="snowball":
                        tk = SnowballStemmer(self.stop_words).stem(tk)
                    elif self.base_form=="lancaster":
                        tk = LancasterStemmer().stem(tk)                        
                    if (self.pos is None) or (token.pos_ in self.pos) or (tk in self.save_words):
                        tokens.append(tk)
                    else:
                        pass
            else:
                if self.base_form=="lemma":
                    tk = token.lemma_
                    if token.lemma_=="n't":
                        tk="not"   
                elif self.base_form=="porter":
                    tk = PorterStemmer().stem(tk)
                elif self.base_form=="snowball":
                    tk = SnowballStemmer().stem(tk)
                elif self.base_form=="lancaster":
                    tk = LancasterStemmer().stem(tk)
                if (self.pos is None) or (token.pos_ in self.pos) or (tk in self.save_words):
                    tokens.append(tk)
                else:
                    pass
        if self.ngram==1:
            result = tokens
        elif self.ngram>1:
            temp=zip(*[tokens[i:] for i in range(0,self.ngram)])
            result = [' '.join(ngram) for ngram in temp]
        else:
            result = tokens
        return result

    def cleanText(self, text):
        sentence = str(text)
        #Removes unicode strings like "\u002c" and "x96"        
        sentence = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', sentence)
        sentence = re.sub(r'[^\x00-\x7f]',r'',sentence)        
        #remove exclamation & question marks
        sentence = re.sub(r"(\!)+", ' ', sentence)
        sentence = re.sub(r"(\?)+", ' ', sentence)   
        #remove punctuation
        sentence = re.sub(r"(\,)+", ' ', sentence)
        sentence = re.sub(r"(\;)+", ' ', sentence)
        sentence = re.sub(r"(\:)+", ' ', sentence)
        #remove parentheses
        sentence = re.sub(r"(\()+", ' ', sentence)
        sentence = re.sub(r"(\))+", ' ', sentence)
        #remove underscore
        sentence = re.sub(r"(\_)+", ' ', sentence)    
        #remove other simbols        
        sentence = re.sub(r"(\-)+", ' ', sentence)
        sentence = re.sub(r"(\+)+", ' ', sentence)
        sentence = re.sub(r"(\/)+", ' ', sentence)
        sentence = re.sub(r"(\*)+", ' ', sentence)
        sentence = re.sub(r"( \')+", ' ', sentence)
        sentence = re.sub(r"(\")+", ' ', sentence)
        sentence = re.sub(r"(\#)+", ' ', sentence)
        sentence = re.sub(r"(\>)+", ' ', sentence)
        sentence = re.sub(r"(\<)+", ' ', sentence)
        sentence = re.sub(r"(\£)+", ' ', sentence)
        sentence = re.sub(r"(\$)+", ' ', sentence)
        sentence = re.sub(r"(\%)+", ' ', sentence)
        sentence = re.sub(r"(\&)+", ' ', sentence)
        sentence = re.sub(r"(\€)+", ' ', sentence)
        sentence = re.sub(r"(\=)+", ' ', sentence)
        sentence = re.sub(r"(\^)+", ' ', sentence)
        #trim
        sentence = sentence.strip('\'"')
        #Remove additional white spaces
        sentence = re.sub('[\s]+', ' ', sentence)
        sentence = re.sub('[\n]+', ' ', sentence)
        sentence = sentence.strip()
        text = sentence
        return text

# %%

"""

import spacy
from nltk.corpus import stopwords
import string

textProc = textProcessing(spacyNLP=spacy.load('en_core_web_sm')
    , stop_words_list=stopwords.words("english")
    , punctuation=list(string.punctuation)
    , base_form="lemma", pos_filter=None, clean_all=True, ngram=1)

"""

# %%
