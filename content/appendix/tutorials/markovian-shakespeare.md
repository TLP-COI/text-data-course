---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Coconut [conda env:text-data]
  language: coconut
  name: conda-env-text-data-coconut
---

```{code-cell} coconut
---
slideshow:
  slide_type: skip
---
from tlp.data import DataLoader
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```

+++ {"slideshow": {"slide_type": "slide"}}

# Markovian Shakespeare

+++ {"slideshow": {"slide_type": "slide"}}

## The Pattern

```{code-cell} coconut
---
slideshow:
  slide_type: '-'
---
patt = re.compile(
    "(?:\A|\n\n)"  # beginning of file or two newlines
    "(^[A-Z][\w ]+):$"  # capital start, colon end
    "\n([\s\S]+?)"  # ANYTHING, but lazy
    "(?=\n\n|\Z)",  # until you hit two newlines or end-of-file
    flags=re.M
)
```

+++ {"slideshow": {"slide_type": "subslide"}}

## The Data

```{code-cell} coconut
---
slideshow:
  slide_type: '-'
---
df = (DataLoader.tiny_shakespeare() 
 |> patt.findall
 |> pd.DataFrame.from_records$(columns=['speaker', 'dialogue'])
 |> .rename_axis(index='line')
)
df
```

+++ {"slideshow": {"slide_type": "slide"}}

## "Importance"?

+++ {"slideshow": {"slide_type": "subslide"}}

### Speaker Frequency?

```{code-cell} coconut
---
cell_style: split
slideshow:
  slide_type: '-'
---
df.speaker.value_counts().plot.hist()
plt.axvline(df.speaker.value_counts().median(), color='r', ls='--')
print('median lines', df.speaker.value_counts().median())
```

```{code-cell} coconut
---
cell_style: split
slideshow:
  slide_type: '-'
---
df.speaker.value_counts()
```

```{code-cell} coconut
---
slideshow:
  slide_type: subslide
---
df.dialogue.str.lower().str.findall(r'\b(\w\w+)\b').explode().value_counts()
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Markov Model

```{code-cell} coconut
---
slideshow:
  slide_type: '-'
---
import pomegranate as pg
model = (df.dialogue.str.lower()#.str.findall(r'\b(\w\w+)\b')
 |> .tolist()
 |> pg.MarkovChain.from_samples$(k=3)
)
```

```{code-cell} coconut
---
slideshow:
  slide_type: subslide
---
for i in range(5):
    model.sample(100)|> ''.join |> print$('\n---\n')
```

```{code-cell} coconut
---
slideshow:
  slide_type: subslide
---
model.distributions[0].keys()|> ', '.join |> print

model.distributions[1]
```

```{code-cell} coconut
---
slideshow:
  slide_type: slide
---
def ecdf(x):
    x = np.sort(x)
    n = len(x)
    def _ecdf(v):
        # side='right' because we want Pr(x <= v)
        return (np.searchsorted(x, v, side='right') + 1) / n
    return _ecdf
def ecdf_tf(s):
    return ecdf(s)(s)

df_prob = (df
 .assign(logprob=df -> df.dialogue.str.lower().apply(model.log_probability))
 .assign(mean_prob=df -> df['logprob']/df.dialogue.str.len())
 .assign(rarity=df -> ecdf_tf(-df['mean_prob']))
 .assign(importance=df -> df['rarity']*ecdf_tf(df.groupby('speaker').speaker.transform('count')))
) 

df_prob
```

```{code-cell} coconut
---
slideshow:
  slide_type: subslide
---
def get_stat_order(df, colname, topn=50): 
    return (
        df[df.speaker.isin(common_speakers)]
        .groupby('speaker')[colname]
        .median().sort_values(ascending=False)
        .index.tolist()
    ) where:
        common_speakers = (
            df.speaker.value_counts()
            |> s-> s[s>=50]
            |> .index.tolist()
        )
        
```

```{code-cell} coconut
---
hide_input: true
slideshow:
  slide_type: subslide
---
sns.catplot(
    data=df_prob, 
    y='speaker', x='rarity', kind='box',
    orient='h', height=10, aspect=.5, color='grey',
    order=get_stat_order(df_prob, 'rarity')
)
```

```{code-cell} coconut
---
hide_input: true
slideshow:
  slide_type: subslide
---
sns.catplot(
    data=df_prob, 
    y='speaker', x='importance', kind='box',
    orient='h', height=10, aspect=.5, color='grey',
    order=get_stat_order(df_prob, 'importance')
)
```

```{code-cell} coconut
tidy = (df
 .assign(token=df.dialogue.str.lower().str.findall(r'\b(\w\w+)\b'))
 .explode(['token'])
 .reset_index()
)
tidy
```

```{code-cell} coconut
tidy.groupby('line').size()
```

```{code-cell} coconut

tf = tidy.groupby(['line', 'token']).token.transform('count')
df = tidy.groupby('token')['line'].transform('size')
N = tidy['line'].nunique()
idf = np.log(N/df)
tidy.assign(tfidf=tf*idf)
```

```{code-cell} coconut

```
