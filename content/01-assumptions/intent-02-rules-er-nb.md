---
jupytext:
  formats: ipynb,md:myst
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

+++ {"slideshow": {"slide_type": "slide"}}

# Rules for Entities, Rules for Relations

+++ {"slideshow": {"slide_type": "subslide"}}

We've used words like _content_ and _keywords_ to refer to "stuff we're interested in", so let's come up with a more unified term. 

Entity
:  Something that exists independently, and is uniquely identifiable. _A thing we're interested in that exists._

In the case of our tokens, many of the tokens-of-interest were words instantiating some _entity_. 
Like tokens, entities can have _types_: e.g. `London` and `New York` are both entities about a location, so `location` is an entity type.

+++ {"slideshow": {"slide_type": "subslide"}}

In addition, we often know something useful about _how entities relate to one another_. 

Relation
:  captures how entities are related to one another
    
This should be familiar from e.g. data modeling. If not, one way to think of this is 
- entities ≈ nouns
- relations ≈ verbs

+++ {"slideshow": {"slide_type": "subslide"}}

In this section, we'll take a look at how people systematically write down and apply **rules** for finding entities and relations.

+++ {"slideshow": {"slide_type": "slide"}}

## Entity Legos: Regular Expressions (RegEx)

+++ {"slideshow": {"slide_type": "subslide"}}

![](https://imgs.xkcd.com/comics/regular_expressions.png)

+++ {"slideshow": {"slide_type": "subslide"}}

Recall the example above: 
> we _missed_ keyword occurrences in the text when the **case** was not taken into acount

Hard-coding "lowercase", while a viable option, case is only the tip of the text-variation iceberg. The answer to 
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

Regex also has several _special characters_ ,e.g. ...

characters inside square brackets `[ ]` or patterns separated with `|`  are _options_. 

  |pattern|meaning| example|
  |---|---|---|
  |`[Tt]h` |"the" with upper or lower `t`| **The** end of **the** road| 
  |`[tT]he\|end`| either `[Tt]he` or `end` | **The end** of **the** road|

+++ {"slideshow": {"slide_type": "subslide"}}

**Character classes**

| meaning              | syntax   |
|----------------------|----------|
| character set        | `[ABC]`  |
| negated set          | `[^ABC]` |
| range                | `[A-Z]`  |
| dot (non-break)      | `.`      |
| unicode              | `\X`     |
| word (alpha, num, _) | `\w`     |
| not word             | `\W`     |
| digit, not digit     | `\d, \D` |
| whitespace, not      | `\s, \S` |
| hspace, not          | `\h, \H` |
| vspace, not          | `\v, \V` |
| line break, not      | `\R, \N` |

+++ {"slideshow": {"slide_type": "subslide"}}

**Anchors** 

These match _positions_, not characters!

| meaning               | syntax   |
|-----------------------|----------|
| beginning             | `^`      |
| end                   | `$`      |
| string begin          | `\A`     |
| string end            | `\Z`     |
| string end (no \n)    | `\z`     |
| word boundary, not    | `\b, \B` |
| end of last match     | `\G`     |

+++ {"slideshow": {"slide_type": "subslide"}}

**Escaped Characters**

Special meanings, so chararcter needs escaping

| meaning           | syntax             |
|-------------------|--------------------|
| reserved          | `+*?^$\.[]{}()\|/` |
| escape reserved   | `\`+reserved       |
| escape multiple   | `\Q` ... `\E`      |
| tab               | `\t`               |
| line feed, return | `\n`               |
| carriage return   | `\r`               |

+++ {"slideshow": {"slide_type": "subslide"}}

**Capture Groups**

"hold on" to patterns for later, or group tokens into a single, bigger pattern. 

| meaning           | syntax                       |
|-------------------|------------------------------|
| capture group     | `(`ABC`)`                    |
| reference group   | `\1`(`$1`), `\2`(`$2`), etc. |
| named group       | `(?'`name`'` ABC`)`          |
| reference name    | `\k'`name`'`                 |
| non-capture group | `(?:`ABC`)`                  |

For other things like atomic groups, branch resets, or subroutine definitions, see a regex reference manual or webpage! :)

+++ {"slideshow": {"slide_type": "subslide"}}

**Lookaround**

sometimes you want to make sure stuff does or does not "exist", but don't _need_ that stuff, itself. 

| meaning             | syntax       |
|---------------------|--------------|
| positive lookahead  | `(?=`ABC`)`  |
| negative lookahead  | `(?!`ABC`)`  |
| positive lookbehind | `(?<=`ABC`)` |
| negative lookbehind | `(?<!`ABC`)` |
| discard until       | `\K`         |

E.g. `(?=New )York` will return the match `York`, but only when it sees `New ` in front of it. 

Be careful, not all languages' regex implementations support all of these!

+++ {"slideshow": {"slide_type": "subslide"}}

**Quantifiers & Alternation**

How much of something? Also, boolean operations (kinda...)

| meaning            | syntax                        |
|--------------------|-------------------------------|
| one-or-more (plus) | ABC`+`                        |
| Any amount (star)  | ABC`*`                        |
| quantifier         | `{`n`}` or `{`start`,`stop`}` |
| 0 or 1 (optional)  | `?`                           |
| make lazy          | quantifier+`?` (e.g. `+?`)    |
| alternation (OR)   | `\|`                          |

These are _incredibly_ useful, since you can build sophisticated patterns using smaller, specific building blocks: 

> Entity Legos!

+++ {"slideshow": {"slide_type": "subslide"}}

**Flags**

Configuration for the regex parser. 

| meaning       | syntax |
|---------------|--------|
| ignore case   | `i`    |
| global search | `g`    |
| multiline     | `m`    |
| dotall        | `s`    |
| no literal ws | `x`    |
| ungreedy      | `U`    |

Use depends on implementation: 
- after the pattern (e.g. in vim): `/pattern/gms`
- as an Enum kwarg (in Python): `re.S`, `re.M`, etc.

+++ {"slideshow": {"slide_type": "subslide"}}

**References** 

- Need Practice? [Rgex Golf](https://alf.nu/RegexGolf) is pretty fun!
    - get the matches, ignore the false matches
    - as _few_ characters in the pattern as possible
    
- Need help? [regexr.com](https://regexr.com)
    - Docstrings and examples for all you just saw
    - add unit tests (like "golf" to pass/fail)
    - get auto explanations for _why_ something matches

+++ {"slideshow": {"slide_type": "subslide"}}

**Discussion**: 
    
What is this for?

```([ab]*)c\1```

```{code-cell} ipython3
---
hide_input: false
slideshow:
  slide_type: fragment
---
# Try below: 
import re
patt = re.compile(r'([ab]*)c\1')
patt.match('aabcaab')
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
patt.match('aabcbaa')
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
patt.findall('aabcaab aabcbaa')
```

+++ {"slideshow": {"slide_type": "subslide"}}

### A (pedantic note)

That example isn't actually "regular", in a computer-science sense. 
It isn't even "context-free". 

**regular expression** comes from Chomsky's Hierarchy, in that it defines a _regular language_ (the strictest subset, below _context-free_). 
A regular language is equivalent to a language that can be recognized by a finite automoton. 

What we just witnessed (exact-string memory of a group instance) was _not_ context-free, or regular. 

> modern RegEx implementations are majorly "souped-up" with convenience features!

+++ {"slideshow": {"slide_type": "slide"}}

## Take a Break (Exercises)

- Write an expression to match markdown sections, to return `(hashes, header, content)` pairs. 
  > _tip: use "multiline"`re.M` and "dotall" `re.S` flags_

- Write expressions to match _Wordle_ words, given feedback
  > _tip: how can we make boolean "AND" in regex?_

```{code-cell} ipython3
---
hide_input: true
slideshow:
  slide_type: skip
---
patt = re.compile(
    "(^#+)"  # the header hashes
    "\s([\w -:]*)"  # the title
    "\s+(.*?)"  # the body content
    "(?=^#|\Z)", # do not include the next section header!
    flags=re.S | re.M
)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
# FIND `patt` SUCH THAT: 
matches = patt.findall(
    """
# This is a Markdown Title
this is _italicized content_.

## This is a Level 2 Subtitle
What more is there to say?
"""
)
import pandas as pd
pd.DataFrame.from_records(matches, columns=['level', 'title', 'content'])
# for match in matches: 
#     print('heading lvl:',match[0])
#     print('title: ',  match[1])
#     print('content: ',match[2])
```

+++ {"slideshow": {"slide_type": "slide"}}

## Relational Pedantry: Ontology

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---

```

+++ {"slideshow": {"slide_type": "subslide"}}

### WordNet

+++ {"slideshow": {"slide_type": "subslide"}}

### ConceptNet

+++ {"slideshow": {"slide_type": "subslide"}}

### Implementation Details
- skos and owl
- jsonschema and jsonld
- struggles and future: linkml(?)
