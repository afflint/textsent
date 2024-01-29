import spacy
from sklearn.feature_extraction.text import CountVectorizer
import re


def spacy_tokenizer(nlp: spacy.language.Language, text: str, lowercase: bool = False, lemma: bool = False, pos_filter: list = None):
    def tolower(w):
        if lowercase:
            return w.lower()
        else:
            return w
    def pos_f(w):
        if pos_filter is None:
            return True
        else:
            return not w.pos_ in pos_filter
    if lemma:
        attr = 'lemma_'
    else:
        attr = 'text'
    tokens = []
    t = re.sub("\s\s+" , " ", text)
    t = re.sub("[\n]+", " ", t)
    t = re.sub("[\r\n]+", " ", t)
    doc = nlp(t)
    for token in doc:
        if pos_f(token):
            tokens.append(tolower(token.__getattribute__(attr)))
    return tokens 


def spacy_count_vectorizer(nlp: spacy.language.Language, documents: list[str], 
                        lowercase: bool = False, lemma: bool = False, pos_filter: list = None, min_df: int = 1):
    tok = lambda x: spacy_tokenizer(nlp, x, lowercase=lowercase, lemma=lemma, pos_filter=pos_filter)
    vectorizer = CountVectorizer(tokenizer=tok, token_pattern=None, min_df=min_df)
    X = vectorizer.fit_transform(documents)
    return X, vectorizer