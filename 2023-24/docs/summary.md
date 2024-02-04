## Notes for the lectures of 5th and 6th of February

### Recap

- We have seen how we can address polarity classification by using a sentiment lexicon
- However, we discussed two main limitations of this approach:
  - 1. Polarity (as well as meaning) is often expressed by more than one word (context)
       1.  *the experience almost frightened me away for **good***
       2.  *the food yesterday was very **good***
    2. The order of words in a sentence is important
       1. *John loves Mary*
       2. *Mary loves John*
    3. Similar words may have a similar polarity (or meaning) but, given a word in the lexicon, it may happen that words similar to it are not also in the lexicon. We need to **generalize** observations.

### Dealing with the order of words

We can deal with the order of words by exploiting **n-grams**.

- Pro: 
  - useful for some relevant sub-sequences
  - provides a first notion of context
- Cons:
  - vocabulary becomes even more sparse
  - we do not generalize
  - very difficult to observe long sub-sequences a relevant number of times (i.e., we can do this just for small *n*)

##### Mutual information to filter meaningful n-grams

$$
MU(w_i, \dots, w_{i+n}) = P(w_i, \dots, w_{i+n})\log \left(\frac{P(w_i, \dots, w_{i+n})}{\prod\limits_{j=i}^{i+n}P(w_j)}\right)
$$

##### Generalization by MU (or alternatively by co-occurrence)

We can also use this kind of relation between pair of words to associate each word $w_i$ with a vector $\mathbf{w}_i \in \mathbb{R}^{V}$ (where $V$ is the size of the vocabulary), such that $\mathbf{w}_i[j] = MU(w_i, w_j)$.

For more on this, look at [github](https://github.com/afflint/textsent/blob/master/2023-24/yelp/n-grams.ipynb)

### Text as a chain of conditional probabilities

With MU and co-occurrences we basically work on the idea of measuring the joint probability of the two words being used together. But there's more in the way we write and think text. In particular, **we can think of the text as a sequence of words that is generated progressively, choosing each word not independently of the others, but on the basis of the sequence generated up to that moment**. Formally:

**LANGUAGE MODEL**
$$
P(w_1, \dots, w_n) = P(w_1)P(w_2 \mid w_1)P(w_3 \mid w_1, w_2), \dots, P(w_n \mid w_1, \dots, w_{n-1}) = \prod\limits_{i=1}^{n} P(w_i \mid w_1, \dots w_{i-1})
$$
This way, the joint probability of a text sequence is reduced to a chain of conditional probabilities. We can use this model to perform two main tasks:

1. Compute the probability of a given sequence of text according to the model
2. Generate a new text starting from the model as follows

**Generative model**

```python
text, V = [], vocabulary including special start end tokens
token = start
while token != end:
  text.append(token)
  token = sample from V according to P(w | text)
```

### Statistical language models

In order to implement the LM idea, we need to estimate $P(w_i \mid w_1, \dots, w_{i-1})$ for each arbitrary word sequence $w_1, \dots w_{i-1}$. We can compute such probabilities from a **training corpus** by exploiting word frequency.
$$
P(w_i \mid w_1, \dots w_{i-1}) = \frac{count(w_1, \dots, w_{i})}{\sum\limits_{j = 1}^{\mid V \mid} count(w_1, \dots, w_j)} = \frac{count(w_1, \dots, w_{i})}{ count(w_1, \dots, w_{i-1})}
$$
**Note**

As an important property of such a model, note that this is completely corpus-dependent. This means that the same LM trained on different corpora result in two different models, with peculiar probabilities for sequences. This way, **we learn the specific language of the corpus**.

However, this approach is highly unfeasible for two main reasons:

1. keeping an index of the frequency of any word sequence in a corpus is too expensive in terms of computation and memory
2. long sequences are highly unfrequent even in large corpora

### Markov Language Models

To deal with the limits of statistical LMs, we adopt a **Markov assumption** that states that each word $w_i$ in the sequence does not depends on the whole previous subsequence, but only from a part of it, the closest to $w_i$ of size $m$, where $m$ is an hyperparameter of the model.

Formally:
$$
P(w_1, \dots, w_n) = \prod\limits_{i=1}^{n} P(w_i \mid w_{i-m}, \dots w_{i-1})
$$
This way, we need just to create indexes for sub-sequences of size $m$ and $m+1$. 