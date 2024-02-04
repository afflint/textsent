from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import numpy as np 
import pandas as pd 
from collections import defaultdict
from copy import deepcopy


class NaiveMarkovLM:
    def __init__(self, n: int = 2) -> None:
        self.n_grams = defaultdict(lambda: defaultdict(lambda: 0))
        self.n = n 
    
    def train(self, documents: list[str]):
        for document in documents:
            for sentence in sent_tokenize(document):
                tokens = word_tokenize(sentence.lower())
                for subsequence in nltk.ngrams(tokens, n=self.n, 
                                            pad_left=True, pad_right=True, 
                                            left_pad_symbol="#S", right_pad_symbol='#E'):
                    prefix = subsequence[:-1]
                    self.n_grams[prefix][subsequence[-1]] += 1
    
    @property
    def index(self):
        return pd.DataFrame(self.n_grams).fillna(0)
    
    def P(self, *args, log: bool = False):
        seq = tuple(args)
        sub = seq[:-1]
        seq_data = self.n_grams[sub]
        # laplace smoothing
        if len(seq_data) == 0:
            t, n = 1, 1
        else:
            t = sum(seq_data.values()) + len(seq_data)
            n = seq_data[seq[-1]] + 1
        if log:
            return np.log(n / t)
        else:
            return n / t 
    
    def joint_log_probability(self, text: list[str]):
        probs = []
        for subsequence in nltk.ngrams(text, n=self.n, 
                                            pad_left=True, pad_right=True, 
                                            left_pad_symbol="#S", right_pad_symbol='#E'):
            probs.append(self.P(*subsequence, log=True))
        return sum(probs)
    
    def generate(self, prefix: tuple[str] = None, max_len: int = 100):
        if prefix is None:
            prefix = ('#S', '#S')
        else:
            prefix = prefix
        count = len(prefix)
        for token in prefix:
            yield token
        while prefix[-1] != '#E' and count <= max_len:
            options = self.n_grams[prefix]
            words, probs = [], []
            for k, _ in options.items():
                words.append(k)
                probs.append(self.P(*prefix, k, log=False))
            next = np.random.choice(words, p=probs)
            count += 1
            yield next
            prefix = tuple(list(prefix[1:]) + [next])
    
    def clone(self):
        c = NaiveMarkovLM(n=self.n)
        c.n_grams = deepcopy(self.n_grams)
        return c 