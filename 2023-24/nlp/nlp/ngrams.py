import nltk
from collections import defaultdict
import numpy as np 
import pandas as pd 


def n_gram_index(corpus: list[str], n: int):
    n_index = defaultdict(lambda: 0)
    for tokens in corpus:
        for gram in nltk.ngrams(tokens, n=n):
            n_index[gram] += 1
    return pd.Series(n_index)