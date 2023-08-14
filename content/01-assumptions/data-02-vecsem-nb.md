---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: text-data
  language: python
  name: text-data
---

# Vector Semantics

```{code-cell} ipython3
import spacy
import numpy as np
from scipy.spatial import distance
# from gensim.models import Word2Vec
import nltk
import pandas as pd
import flair
```

```{code-cell} ipython3
# !python -m spacy download en_core_web_md
# nlp=spacy.load('en_core_web_md')
from flair.embeddings import WordEmbeddings
from flair.data import Sentence

# init embedding
glove_embedding = WordEmbeddings('glove')
```

```{code-cell} ipython3
# create sentence.
sentence = Sentence('The grass is green .')

# embed a sentence using glove.
glove_embedding.embed(sentence)

# now check out the embedded tokens.
for token in sentence:
    print(token)
    print(token.embedding)
```

```{code-cell} ipython3
def vec(s:str):
    return nlp(s).vector
vec('lion')
```

```{code-cell} ipython3
your_word = "lion"

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)
```

```{code-cell} ipython3
# Format the vocabulary for use in the distance function
words = pd.Series(list(nlp.vocab.vectors.strings)).str.lower().pipe(
    lambda s: s[s.str.fullmatch('[a-z]+')]
).unique()
vocab_vectors = np.array([nlp.vocab.strings[nlp.vocab.vectors[x]] for x in words])
## use nltk
```

```{code-cell} ipython3
vocab_vectors@vocab_vectors.T
```

```{code-cell} ipython3

```

```{code-cell} ipython3
# input_word = "frog"
# p = np.array([nlp.vocab[input_word].vector])
p = np.array([vec('king')+vec('queen')-vec('man')])
# *** Find the closest word below ***
closest_index = distance.cdist(p, vocab_vectors).argmin()
word_id = list(nlp.vocab.vectors.keys())[closest_index]
nlp.vocab[word_id].text
# output_word is identical, or very close, to the input word
```

```{code-cell} ipython3
np.ndarray.argsort
```
