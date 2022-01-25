# %%
#   Packages
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
import string

# %%
class textProcessing(object):
    
    def __init__(self, model='en_core_web_sm', base_form="lemma", pos_filter=None, clean_all=True, stop_words="english", ngram = 1):
        """
        base_form:
            + lemma -> retrieve spaCy lemma
            + porter -> retrieve nltk PorterStemmer
            + snowball -> retrieve nltk SnowballStemmer
            + lancaster -> retrieve nltk LancasterStemmer        
        """
        self.nlp = spacy.load(model)
        self.base_form = base_form
        self.pos = pos_filter
        self.clean_all = clean_all
        self.stop_words = stop_words
        self.punctuation = list(string.punctuation)
        self.ngram = ngram
    
    def filteredToken(self, text):
        tokens = []
        if self.stop_words!=False:
            self.stop_words_list = stopwords.words(self.stop_words)
        for token in self.nlp(text):
            if self.clean_all:
                if (token.text not in self.punctuation) and (token.text not in self.stop_words_list):
                    if self.base_form=="lemma":
                        tk = token.lemma_
                    elif self.base_form=="porter":
                        tk = PorterStemmer().stem(token.text)
                    elif self.base_form=="snowball":
                        tk = SnowballStemmer(self.stop_words).stem(token.text)
                    elif self.base_form=="lancaster":
                        tk = LancasterStemmer().stem(token.text)
                    else:
                        tk = token.text
                    if (self.pos is None) or (token.pos_ in self.pos):
                        tokens.append(tk.lower())
                    else:
                        pass
            else:
                if self.base_form=="lemma":
                    tk = token.lemma_
                elif self.base_form=="porter":
                    tk = PorterStemmer().stem(token.text)
                elif self.base_form=="snowball":
                    tk = SnowballStemmer().stem(token.text)
                elif self.base_form=="lancaster":
                    tk = LancasterStemmer().stem(token.text)
                else:
                    tk = token.text
                if (self.pos is None) or (token.pos_ in self.pos):
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

# %%