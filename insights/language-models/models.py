from collections import defaultdict, Counter

import numpy as np
from nltk import ngrams, pad_sequence
from tqdm import tqdm


class NGramModel(object):
    """
    Assumes tokens as numerical indexes
    """

    def __init__(self, n=3, eos=102):
        self.ngrams = defaultdict(Counter)
        self.n = n
        self.eos = eos

    def count_ngrams(self, sentences):

        """ Collect ngram counts from corpus of sentences. """

        for sentence in tqdm(sentences):
            for ngram in ngrams(sentence, n=self.n, pad_left=True, left_pad_symbol=self.eos):
                prefix, next_word = ngram[:-1], ngram[-1]
                self.ngrams[tuple(prefix)][next_word] += 1

    def compute_log_prob(self, prefix):

        """ Compute log probabilities for a given prefix.
        Args:
            prefix List[str]: list of words

        Returns:
            dictinary of log probabilities : dict(tuple, float)

        """

        # if prefix is shorter than n-1 -> pad prefix to n-1 length
        prefix = tuple(pad_sequence(prefix,
                                    n=self.n - 1,
                                    pad_left=True,
                                    left_pad_symbol=0)
                       )
        # if prefix is longer than n-1 -> take the last n-1 grams
        prefix = prefix[-(self.n - 1):]

        # counts for all words that might follow the prefix
        next_word_counts = self.ngrams[prefix]

        # prefix is found among ngrams
        if len(next_word_counts) > 0:
            prefix_counts = sum(self.ngrams[prefix].values())
            return {next_word:
                        np.log(next_word_counts[next_word]) -
                        np.log(prefix_counts) for next_word in next_word_counts}

            # prefix never occurred in training corpus
        else:
            return {}

    def sample_next(self, prefix):
        """
        Sample the next token for a given prefix according to the frequency learned from data.

        Args:
            prefix: List[str]

        Returns:
            next token: int

        """
        next_word_prob = self.compute_log_prob(prefix)
        if len(next_word_prob) > 0:
            next_token, next_prob = next_word_prob.keys(), next_word_prob.values()
            end = np.random.choice(list(next_token), p=np.exp(list(next_prob)))
            return end
        return self.eos

    def eval_prob(self, sentence):
        p = float('-inf')
        for chunk in ngrams(sentence, n=self.n, pad_left=True, left_pad_symbol=self.eos):
            prefix = chunk[-self.n:-1]
            count = self.ngrams[prefix][chunk[-1]]
            if count > 0:
                p = np.log(count) - np.log(sum(self.ngrams[prefix].values()))
                p += p
        return p
