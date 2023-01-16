from collections import Counter, defaultdict
from typing import Callable

import numpy as np
import pandas as pd


class InMemoryCountIndex(object):

    def __init__(self, tokenizer: Callable):
        self.tokenizer = tokenizer
        self.index = defaultdict(lambda: {})
        self.docs_size = []
        self.unique_words_history = []
        self.occurrences = 0

    def add(self, document: str):
        doc_id = len(self.docs_size)
        self.docs_size.append(len(document))
        for token, count in Counter(self.tokenizer(document)).most_common():
            self.index[token][doc_id] = count
            self.occurrences += count
        self.unique_words_history.append(len(self.index))

    def to_sparse_matrix(self):
        return pd.DataFrame(self.index).fillna(0)

    def p(self, token):
        count = sum(self.index[token].values())
        try:
            prob = count / self.occurrences
        except ZeroDivisionError:
            prob = np.nan
        return prob
