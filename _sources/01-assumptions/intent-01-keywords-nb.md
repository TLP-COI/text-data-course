---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell}
---
slideshow:
  slide_type: skip
tags: [remove-cell]
---
%reload_ext coconut
```

```{code-cell}
---
slideshow:
  slide_type: skip
tags: [remove-cell]
---
%%HTML
<link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.min.css" rel="stylesheet" type="text/css" />
```

+++ {"slideshow": {"slide_type": "slide"}}

# Keywords 

> "Quality Content" and Where to Find It...

+++ {"slideshow": {"slide_type": "subslide"}}

The first step toward quantifying _something_ is to ask quantifying questions about it

+++ {"slideshow": {"slide_type": "fragment"}}

> What? How much? How many? How often?

+++ {"slideshow": {"slide_type": "fragment"}}

These questions help form a narrative (what am I interested in?), and _sell_ that narrative (why should I be interested?)

In essence, we are looking for good _content_, the "stuff" that is useful or interesting from the

+++ {"slideshow": {"slide_type": "slide"}}

## Keywords

+++ {"slideshow": {"slide_type": "subslide"}}

Let's grab one of our course datasets: MTGJson, as documented [in the appendix](content/appendix/datasets/mtgjson). If you're following along, DVC can grab the data, as well: `dvc import...`

```{code-cell}
---
slideshow:
  slide_type: fragment
---
from tlp.data import DataLoader
df = DataLoader.mtg()
```

```{code-cell}
---
hide_input: true
slideshow:
  slide_type: subslide
---
from tlp.data import mtg, styleprops_longtext

(df[['name', 'text','flavor_text']]
 .sample(10, random_state=2).fillna('').style
 .set_properties(**styleprops_longtext(['text','flavor_text']))
 .hide_index()
)
```

+++ {"slideshow": {"slide_type": "subslide"}, "cell_style": "split"}

_Flavor text_ has been a staple of Magic cards for a long time. 
A lot of players gravitate to it, even more than the game itself. 

There are easter-eggs, long-running gags, and returning characters. 
Flavor text is really cool. 

That sounds like some interesting "content"...what is its history?

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}, "tags": ["margin"]}

{figure-md} feeling-lost
![fblthp](https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/c/c4/Fblthp.jpg)

_Magic: The Gathering_ can be a lot to take in, and it's easy to get lost in all the strange words. 
This is why we use it for TLP! 
Thankfully, us "lost" folks have a mascot, in old Fblthp, here!

```{code-cell}
---
slideshow:
  slide_type: subslide
---
import pandas as pd
import numpy as np
import hvplot.pandas
(df
 .set_index('release_date')
 .sort_index()
 .resample('Y')
 .apply(lambda grp: grp.flavor_text.notna().sum()/grp.shape[0])
#  .apply(lambda grp: )
).plot( rot=45, title='What fraction of cards have Flavor Text each year?')
```

+++ {"slideshow": {"slide_type": "subslide"}}

There's a lot of other data avaliable, as well!

```{code-cell}
---
slideshow:
  slide_type: '-'
---
mtg.style_table(df.sample(10, random_state=2),
                        hide_columns=['text','flavor_text'])
```

```{code-cell}
---
cell_style: split
hide_input: false
slideshow:
  slide_type: subslide
---
import matplotlib.pyplot as plt

def value_ct_wordcloud(s: pd.Series):
    from wordcloud import WordCloud
    wc = (WordCloud(background_color="white", max_words=50)
          .generate_from_frequencies(s.to_dict()))
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

(df.types.explode().value_counts()
 .pipe(value_ct_wordcloud)
)
```

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

What "types" of cards are there?
What are the "subtypes" of cards, and how are they differentiate from "types"?


It looks like this magic is quite anthropocentric!

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: '-'
---
(df.subtypes.explode().value_counts()
 .pipe(value_ct_wordcloud) 
)
# df.subtypes.value_counts()
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Keywords**

These kinds of comma-separated lists of "content-of interest" are generally called keywords. 
Here, we have been _told_ what those keywords are, which is nice!

Question... would we always have been able to find them from the text?

```{code-cell}
---
cell_style: split
hide_input: true
slideshow:
  slide_type: '-'
---
def plot_textual_occurrence(
    df,
    key_col='keywords', 
    txt_col='text',
    pre = str # do nothing, make str
): 

    def keyword_in_txt(df_row):
        return (
            pre(df_row[key_col]) 
            in 
            pre(df_row[txt_col])
        )

    return (
        df[['text','keywords']].explode('keywords')
        .dropna(subset=['keywords'])
        .assign(
            textual=lambda df: 
            df.apply(keyword_in_txt, axis=1)
        )
        .groupby('keywords').mean()
        .sort_values('textual')
        .head(40)
        .hvplot.barh(
            title='Fraction of text containing keyword',
            frame_width=250, 
            frame_height=350
        )
    )

plot_textual_occurrence(df)
```

```{code-cell}
---
cell_style: split
hide_input: true
slideshow:
  slide_type: fragment
---
# wait...let's lowercase
plot_textual_occurrence(
    df, pre=lambda s: str(s).lower()
)
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Recap

- Content in a document can occur in or alongside the text itself. 
- Keywords are individual markers of useful content, often comma-separated
- Often you need to "tidy up" keyword lists with `df.explode('my_keyword_column)`
- Keywords can be supplied a priori (by experts, etc.) Use them!
- Supplied keywords have become divorced from the text... do they match?

+++ {"slideshow": {"slide_type": "subslide"}}

### Sanity-check

So: 
- `interesting content` $\rightarrow$ `frequent content` 
  
  $\rightarrow$ `frequent keywords`

+++ {"slideshow": {"slide_type": "fragment"}}

_What assumption(s) did we make just then?_

+++ {"slideshow": {"slide_type": "subslide"}}

> - `interesting content` $\rightarrow$ `frequent content` $\rightarrow$ `frequent key`**`words`**

_What are **words**?_

+++ {"slideshow": {"slide_type": "subslide"}}

We are _assuming_ that a "fundamental unit" of interesting content is a "word". 
Remember, though, that a "word" is not a known concept to the computer... all it knows are "strings"

Individual characters, or even slices of strings (i.e. _substrings_) don't have any specific meaning to us as concepts (directly). 
This means there is a fundamental disconnect (and, therefore, a need for _translation_) between strings and words, to allow the assumption above to _work_ in the first place.

```{code-cell}
---
hide_input: true
slideshow:
  slide_type: fragment
---
%%coconut
def substrings(size) = 
    """return a function that splits stuff into 'size'-chunks and prints as list"""
    groupsof$(size)..> map$(''.join) ..> list ..> print

my_str = "The quick brown fox"
my_str |> substrings(3)
my_str |> substrings(4)
my_str |> substrings(5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Only some of these would make sense as "words", and that's only if we do some post-processing in our minds (e.g. `own` could be a word, but is that the same as `[ ]own`?

+++ {"slideshow": {"slide_type": "subslide"}}

How do we: 

- formalize turning strings into the these concept-compatible "word" objects? 
- Apply this to our text, so we know the concepts available to us?

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}

## Intro to Tokenization

+++ {"slideshow": {"slide_type": "subslide"}}

Preferably, we want to replace the `substrings` function with something that looked like: 

```python
substr(my_str)
>>> ['The', 'quick', 'brown', 'fox']
```

In text-processing, we have names for these _units of text_ that communicate a single concept: **tokens**. 
The process of breaking strings of text into tokens is called _tokenization_.

+++ {"slideshow": {"slide_type": "subslide"}}

There's actually a few _special words_ we use in text analysis to refer to meaningful parts of our text, so let's go ahead and define them ({cite}`jurafsky-textbook`): 

**corpus**
: the set of all text we are processing
  > _e.g. the text from entire MTGJSON dataset is our corpus_

**document** 
: a unit of text forming an "observation" that we can e.g. compare to others
  > e.g. each card in MTGJSON is a "document" containing a couple sections of text

+++ {"slideshow": {"slide_type": "subslide"}}

**token**
: a piece of text that stands for a word. 
  > the flavor-text for `Mardu Hateblade`: has 15 tokens, excluding punctuation:
  >
  > _"There may be little honor in my tactics, but there is no honor in losing."_ 

**types**
: unique words in the vocabulary
  > For the same card above, there are 15 tokens, but only 13 types (`there`x2, `honor` x2, `in` x2)

+++ {"slideshow": {"slide_type": "subslide"}}

### Using Pandas' `.str`

There are a number of [very helpful tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) in the pandas `.str` namespace of the `Series` object. We can return to our card example from before:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
card = df[df.name.str.fullmatch('Mardu Hateblade')]
flav = card.flavor_text
print(f'{card.name.values}:\n\t {flav.values[0]}')
# df.iloc[51411].flavor_text
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
flav.str.upper()  # upper-case
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
flav.str.len()  # how long is the string?
```

+++ {"slideshow": {"slide_type": "subslide"}}

**verify**: the number of tokens and types

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# Should be able to split by the spaces...
print(flav.str.split(' '), '\n')
print("no. tokens: ", flav.str.split(' ').explode().size)
print("no. types: ",len(flav.str.split(' ').explode().unique()))
```

+++ {"slideshow": {"slide_type": "fragment"}}

wait a minute...

```{code-cell}
---
slideshow:
  slide_type: subslide
---
flav.str.split().explode().value_counts()
```

+++ {"slideshow": {"slide_type": "-"}}

This isn't right! 

We probably want to split on anything that's not "letters":

```{code-cell}
---
slideshow:
  slide_type: subslide
---
flav.str.split('[^A-Za-z]').explode().value_counts()
```

+++ {"slideshow": {"slide_type": "fragment"}}

Much better!

So what is this devilry? This `[^A-Za-z]` is a pattern --- a _regular expression_ --- for "things that are _not_ alphabetical characters in upper or lower-case". Powerful, right? We'll cover this in more detail in the next section. 

In the meantime, let's take a look again at this workflow pattern:
> `tokenize` $\rightarrow$ `explode`

+++ {"slideshow": {"slide_type": "slide"}}

## Tidy Text

+++ {"slideshow": {"slide_type": "subslide"}}

_but first_...

### Tidy Data Review

+++ {"slideshow": {"slide_type": "subslide"}}

Let's review an incredibly powerful idea from the R community: using _tidy data_. 

Tidy data is a _paradigm_ to frame your tabular data representation in a _consistent_ and _ergonomic_ way that supports rapid manipulation, visualization, and cleaning. Imagine we had this non-text dataset (from Hadley Wickham's paper _Tidy Data_):

```{code-cell}
---
slideshow:
  slide_type: fragment
---
df_untidy = pd.DataFrame(index=pd.Index(name='name', data=['John Smith', 'Jane Doe', 'Mary Johnson']), 
             data={'treatment_a':[np.nan, 16, 3], 'treatment_b': [2,11,1]})
df_untidy
```

+++ {"slideshow": {"slide_type": "subslide"}}

We could also represent it another way:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
df_untidy.T
```

+++ {"slideshow": {"slide_type": "subslide"}}

I'm sure these might be equally likely to see in someone's excel sheet, entering this data. But, say we want to visualize this table? Or start comparing each of the cases? This is going to take a lot of manipulation every time we want a different thing. 

For data to be _Tidy Data_, we need 3 things: 

> 1. Each variable forms a column.
> 2. Each observation forms a row.
> 3. Each type of observational unit forms a table.

```{code-cell}
---
slideshow:
  slide_type: subslide
---
df_tidy = df_untidy.reset_index().melt(id_vars=['name'])
df_tidy
```

+++ {"slideshow": {"slide_type": "fragment"}}

Suddenly things like comparing, plotting, and counting become trivial with simple table operations. 

> But doesn't this waste table space? It's so much less compact!

+++ {"slideshow": {"slide_type": "subslide"}}

That's excel talking! The "wasted space" is incredibly negligible at this scale, compared to the ergonomic benefit of representing your data **long-form**, with one-observation-per-row. Now you get exactly one column for every variable, and one row for every point of data, making your manipulations much cleaner.

```{code-cell}
---
hide_input: false
slideshow:
  slide_type: slide
---
import seaborn as sns
sns.catplot(
    data=df_tidy, 
    y='value', 
    x='name', 
    hue='variable', # try commenting/changing to 'col'!
    kind='bar'
)
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Back to Tidy _Text_

So, hang on, aren't _documents_ our observational-level? Wouldn't that make e.g. the MTGJSON dataset _already "tidy"_??

+++ {"slideshow": {"slide_type": "fragment"}}

Yes! 

But only if we are observing _cards_, which, for things like release date or mana cost, maybe that's true. 

Instead, we are trying to find (observe) the occurrences of "interesting content", which we broke down into _tokens_.

+++ {"slideshow": {"slide_type": "subslide"}}

> _We thus define the tidy text format as being a table with one-token-per-row._
> _A token is a meaningful unit of text, such as a word, that we are interested in using for analysis, and tokenization is the process of splitting text into tokens._
> _This one-token-per-row structure is in contrast to the ways text is often stored in current analyses, perhaps as strings or in a document-term matrix._

```{code-cell}
---
cell_style: split
hide_input: false
slideshow:
  slide_type: subslide
---
%%coconut
import nltk
import janitor as pj
nltk.download('punkt')

tidy_df = (
    df
    .add_column('word', wordlists)
    .also(df -> print(df.word.head(10)))
    .explode('word')
    .rename_axis('card_id')
    .reset_index()
) where: 
    wordlists = (
        df.flavor_text
        .fillna('')
        .str.lower()
        .apply(nltk.tokenize.word_tokenize)
    )
```

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: fragment
---
tidy_df.word.value_counts().head(20)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Assumption Review

+++ {"slideshow": {"slide_type": "subslide"}}

### Words? Stopwords.

> The "anti-keyword"

Stuff that we say, _a priori_ is uninteresting. Usually articles, pasive being verbs, etc.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
nltk.download('stopwords')
stopwords = pd.Series(name='word', data=nltk.corpus.stopwords.words('english'))
print(stopwords.tolist())
```

+++ {"slideshow": {"slide_type": "subslide"}}

**NB**

Discussion: stopwords are _very_ context-sensitive decisions. 

- Can you think of times when these are _not_ good stop words? 

- When would these terms actually imply interesting "content"?

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: subslide
---
(tidy_df
 .filter_column_isin(
     'word',
     nltk.corpus.stopwords.words('english'), 
     complement=True # so, NOT IN
 )
 .word.value_counts().head(30)
)
```

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

This seems to have worked _ok_. 

Now we can see some interesting "content" in terms like "life", "death", "world", "time", "power", etc.

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

> What might we learn from these keywords? What else could we do to investigate them?

+++ {"slideshow": {"slide_type": "subslide"}}

### Importance $\approx$ Frequency?

```{code-cell}
---
slideshow:
  slide_type: subslide
---
%%coconut 
keywords = (
    tidy_df
    .assign(**{
        'year': df -> df.release_date.dt.year,
        'yearly_cnts': df -> df.groupby(['year', 'word']).word.transform('count'),
        'yearly_frac': df -> df.groupby('year').yearly_cnts.transform(grp->grp/grp.count().sum())
    })
    .filter_column_isin(
        'word', 
        ['life', 'death']
#         ['fire', 'water']
    )
)
```

```{code-cell}
---
slideshow:
  slide_type: subslide
---
sns.lineplot(data=keywords, x='year', y='yearly_cnts',hue='word')
```

```{code-cell}
---
slideshow:
  slide_type: subslide
---
sns.lineplot(data=keywords, x='year', y='yearly_frac',hue='word')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Lessons**: 

- Frequency can have _many_ causes, few of which correlate to underlying "importance"
- Starting to measure importance? _relative_ comparisons, ranked. 

This get's us part of the way toward information-theoretic measures, and other common weighting schemes. More to come in the [Measure & Evaluate]() chapter.

+++ {"slideshow": {"slide_type": "slide"}}

## Aside: how many keywords in my corpus?

+++ {"slideshow": {"slide_type": "subslide"}}

> **token**
> : a piece of text that stands for a word. 

> **types**
> : unique words in the vocabulary

So:
- num. types is the size of the vocabulary $\|V\|$
- num. tokens is the size of the corpus $\|N\|$

+++ {"slideshow": {"slide_type": "subslide"}}

Heap's Law: 
$$ \|V\| = k\|N\|^\beta$$

```{code-cell}
# tidy_df.groupby(['card_id']).word.agg(['cumcount', lambda s: (~s.duplicated()).cumsum()])
# (~tidy_df.word.duplicated()).cumsum()
tidy_df.groupby(['card_id']).word.size().cumsum()
```

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: subslide
---
rand = np.random.default_rng()
def sample_docs(df, id_col='card_id', shuffles=5, rng=np.random.default_rng()):
    samps = []
    for i in range(shuffles):
        shuff = df.shuffle()
        samps+=[pd.DataFrame({
            'N': shuff.groupby(id_col).word.size().cumsum(), 
            'V': (~shuff.word.duplicated()).cumsum()
        })]
    return pd.concat(samps).reset_index(drop=True).dropna().query('N>=100')

heaps = sample_docs(tidy_df)
heaps
```

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: fragment
---
from scipy.optimize import curve_fit
def heaps_law(n, k, beta): 
    return k*n**beta

def fit_heaps(data, linearize=False):
    if not linearize:
        params, _ = curve_fit(
            heaps_law,
            data.N.values, 
            data.V.values
        )
    else: 
        log_data = np.log(data)
        params, _ = curve_fit(
            lambda log_n, k, beta: np.log(k) + beta*log_n,
            log_data.N.values,
            log_data.V.values
        )
    return params
```

```{code-cell}
---
cell_style: center
slideshow:
  slide_type: subslide
---
def plot_heaps_law(heaps, log_scale=False, linearize=False):
    params = fit_heaps(heaps, linearize=linearize)
    print(f'fit: k={params[0]:.2f}\tβ={params[1]:.2f}\tlinear-fit={linearize}')
    
    x = np.linspace(100,6e5)
    plt.scatter(heaps.N, heaps.V, )
    plt.plot(
        x, 
        heaps_law(x, params[0], params[1]), 
        color='orange', lw=3, label=f'Heaps\' (β={params[1]:.2f})'
    )
    plt.fill_between(x, 
                     heaps_law(x, params[0], 0.67),
                     heaps_law(x, params[0], 0.75),
                    color='grey', alpha=.2, 
                    label='typical-range')

    plt.ylim(1,heaps.V.max()+1000)
    plt.plot(x, np.sqrt(x), ls='--', label='sqrt', color='k')
    if log_scale:
        plt.xscale('log')
        plt.yscale('log')
    plt.legend()
plot_heaps_law(heaps)
```

+++ {"cell_style": "center", "slideshow": {"slide_type": "subslide"}}

So, our data grows in _complexity_ a lot faster than the square-root of it's size, but slower than "typical" text. 

Most data-sets in NLP are between 0.67-0.75, so we 
- get a lot of complexity early on, but ...
- there's not such an extended amout of "new concepts" to find, after a while. 

> Pretty typical of "technical", or, _synthetic_ and domain-centric language. Lot's of variety _initially_, but limited in scope compared to casual speech.

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: subslide
---
plot_heaps_law(heaps, log_scale=True)
```

```{code-cell}
---
cell_style: split
slideshow:
  slide_type: fragment
---
plot_heaps_law(heaps, log_scale=True, 
               linearize=True)
```

```{code-cell}
plot_heaps_law(heaps, log_scale=False, linearize=True)
```
