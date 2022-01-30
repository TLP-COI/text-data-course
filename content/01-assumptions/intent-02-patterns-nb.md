---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python [conda env:text-data]
  language: python
  name: conda-env-text-data-py
---

# Written Rules

> Do exactly as I say

+++ {"slideshow": {"slide_type": "slide"}}


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

```{code-cell} ipython3
# Try below: 
import re
patt = re.compile('the')
[print(i) for i in  df.text.sample(5, random_state=2).tolist()]
df.text.sample(5, random_state=2).str.count(patt)
# df.text.str.contains('the')
```

+++ {"slideshow": {"slide_type": "slide"}}

## Grammars

> Regex, but _more trees_

+++ {"slideshow": {"slide_type": "slide"}}