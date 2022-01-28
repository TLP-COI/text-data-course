---
jupytext:
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

+++ {"slideshow": {"slide_type": "slide"}}

# Finding Content

+++ {"slideshow": {"slide_type": "notes"}}

:::{tip}
Textbook Reading: [Ch. 2.1-2.4](https://web.stanford.edu/~jurafsky/slp3/2.pdf)
:::

The first step toward quantifying _something_ is to ask quantifying questions about it

+++ {"slideshow": {"slide_type": "subslide"}}

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
import pandas as pd

df = DataLoader.mtg()
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

:::{figure-md} feeling-lost
![fblthp](https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/c/c4/Fblthp.jpg)

_Magic: The Gathering_ can be a lot to take in, and it's easy to get lost in all the strange words. 
This is why we use it for TLP! 
Thankfully, us "lost" folks have a mascot, in old Fblthp, here!
:::

```{code-cell}
---
slideshow:
  slide_type: subslide
---
import hvplot.pandas
(df
 .set_index('release_date')
 .sort_index()
 .resample('Y')
 .apply(lambda grp: grp.flavor_text.notna().sum()/grp.shape[0])
#  .apply(lambda grp: )
).hvplot( rot=45, title='What fraction of cards have Flavor Text each year?')
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

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}

## Regular Expressions (RegEx)

+++ {"slideshow": {"slide_type": "subslide"}}

![](https://imgs.xkcd.com/comics/regular_expressions.png)

+++ {"slideshow": {"slide_type": "subslide"}}

Recall the example above: 
> we _missed_ keyword occurrences in the text when the **case** was not taken into acount

Hard-coding case, while a viable option, is only the tip of the text-variation iceberg. The answer to 
>"How to I find strings that fit some _pattern_ I'm looking for?" 

is almost always 
> **Regular Expressions**

+++ {"slideshow": {"slide_type": "subslide"}}

### What is RegEx

ReGex is a mini-language for writing patterns that you want to find in a bunch of text. The most basic use is to match exact strings: 

|pattern|meaning| example|
|---|---|---|
|`a`| _match character_ `a`| **a**pple|
|`the`| _match string `the`| **the**re went **the** last one!| 

This is the same as what we did above, for keywords: `my_pattern in my_text`. By default, RegEx patterns are case-sensitive! (`A` will not match an `a`)

+++ {"slideshow": {"slide_type": "subslide"}}

Regex also has several _special characters_. 
- Characters inside square brackets `[ ]` or patterns separated with `|`  are _options_. 
  |pattern|meaning| example|
  |---|---|---|
  |`[Tt]h` |"the" with upper or lower `t`| **The** end of **the** road| 
  |`[tT]he\|end`| either `[Tt]he` or `end` | **The end** of **the** road|

+++ {"slideshow": {"slide_type": "fragment"}}

- Inside the start of `[]`, a carat `^` is "NONE OF THESE": `[^T]he` matches `the` and `xhe`, not `The`. 
- Parentheses () are a _match_ group... you will get back stuff that matches inside to use later!
- anhcors: `^`: start of a line, `$`: end of a line
- Special on/off comands with letters/capitals: 
  - `\s` whitespace, `\S` _not_ whitespace
  - `\d` digit, `\D` _not_ digit. 
  - `\w` "word character", `\N` "not word character" (BEWARE)

```{code-cell}
# Try below: 
import re
patt = re.compile('the')
[print(i) for i in  df.text.sample(5, random_state=2).tolist()]
df.text.sample(5, random_state=2).str.count(patt)
# df.text.str.contains('the')
```

+++ {"slideshow": {"slide_type": "slide"}}

## Tokenization

> Quantity has a quality all its own
