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

In this section, we'll take a look at how people systematically express their intent about entities and relations: ways they write **rules** for them.

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

+++ {"slideshow": {"slide_type": "slide"}}

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

+++ {"slideshow": {"slide_type": "notes"}}

note that this matches, but the next one does not:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
patt.match('aabcbaa')
```

+++ {"slideshow": {"slide_type": "notes"}}

This means that the "group" being referened is _evaluated_ before it gets referenced later... `\1` _must_ be `aab` in this case, not `b` (even though that _would_ be a valid match for `[ab]*`).
Our pattern matched on `aab` instead of `b`, so `\1` must match that!

Now, the `findall` function will return _match groups_...in fact, it will find all non-overlapping matches. 
Since `b` is a valid match group, _and_ is duplicated for `\1` to succeed, the `findall` function _will return it_. 
This is different from the `match` function!

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
patt.findall('aabcaab  aabcbaa')
```

+++ {"slideshow": {"slide_type": "subslide"}}

### A (pedantic note)

That example isn't actually "regular", in a computer-science sense. 
It isn't even "context-free". 

**regular expression** comes from Chomsky's Hierarchy, in that it defines a _regular language_ (the strictest subset, below _context-free_). 
A regular language is equivalent to a language that can be recognized by a finite automoton. 

What we just witnessed (exact-string memory of a group instance) was _not_ context-free, or regular. 

> modern RegEx implementations are majorly "souped-up" with convenience features!

+++ {"slideshow": {"slide_type": "slide"}, "hide_input": true}

## Take a Break (Exercises)

- Write an expression to match markdown sections, to return `(hashes, header, content)` pairs. 
  > _tip: use "multiline"`re.M` and "dotall" `re.S` flags_

- Write expressions to match _Wordle_ words, given feedback
  > _tip: how can we make boolean "AND" in regex?_

+++ {"slideshow": {"slide_type": "notes"}}

### Markdown Parser (worked example)
One approach to turning markdown into a table of sections

- group the header "hash" symbols
- group the text that _follows_ the hash symbols
- find all text on the next line(s), EXCEPT: 
- stop when the _next_ line (look-ahead) is another header!

```{code-cell} ipython3
---
hide_input: false
slideshow:
  slide_type: notes
---
patt = re.compile(
    "(^#+)"  # the header hashes
    "\s([\w -:]*)"  # the title (could contain non-word chars)
    "\n+(.*?)"  # the body content
    "(?=^#|\Z)", # do not include the next section header!
    flags=re.S | re.M
)
```

```{code-cell} ipython3
---
hide_input: false
slideshow:
  slide_type: notes
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
```

+++ {"slideshow": {"slide_type": "slide"}}

### Tokenizers

To split text into tokens, we could match patterns for: 
- what _is_ a word? --> `re.findall`
- what is _not_ a word? --> `re.split`

+++ {"slideshow": {"slide_type": "notes"}}

It's worth mentioning that the _token_ we match is not "the same" as the _entity_. 
Rather, we humans are using RegEx as an assumption that pieces of matching text are valid stand-ins to represent the abstract entity, correctly! 

This distinction becomes especially important when our human languages have e.g. [polysemy](https://www.wikiwand.com/en/Polysemy); some _tokens_ should point to completely separate entities, depending on conext.
However, if we assume Regex as a mechanism to find tokens meant to _stand-in_ for entities of interest, that's a _rule_ standing in for our intent. 

+++ {"slideshow": {"slide_type": "subslide"}}

**Whitespace Tokenizer** 

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
my_str = "Isn't this fun? It's time to tokenize!"
re.compile('\s').split(my_str)
```

+++ {"slideshow": {"slide_type": "fragment"}}

This looks pretty good! 
Notice, though, the punctuation is _sometimes_ helpful (it's, isn't), but often adds unnecessary extra ("fun?", "tokenize!", all are ostensibly the same entity as "fun" or "tokenize". |

+++ {"slideshow": {"slide_type": "subslide"}}

**Scikit-Learn-Style Tokenizer**

Very popular way to tokenize text, especially given the intended use-case (statistical NLP, with matrices)

`\b\w\w+\b`

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
re.compile(r"\b\w\w+\b").findall(my_str)
```

+++ {"slideshow": {"slide_type": "fragment"}}

This time, we avoid punctuation, but lose conjunctions. 
It's not uncommon to remove punctuation entirely as a preprocessing step. 

Does that always make sense? 

+++ {"slideshow": {"slide_type": "subslide"}}

### "Technical" Tokens for Technical Entities

A lot of times the above assumptions won't cut it, _especially_ if there are specific technical entities that a token needs to reference. 
Here are a few patterns I have seen in e.g. Maintenance Work Order text: 

+++ {"slideshow": {"slide_type": "-"}, "cell_style": "split"}

| Pattern          | Example    |    Description|
|------------------|------------|---------------|
| `\#[\w\d]+\b`    | `#T43H5sw` | ID's for machines, positions|
| `\b\w[\/\&]\w\b` | `P&G`,`A/C`| Split bigrams, common shorthands|
| `\b\w[\w\'\d]+\b`| `won't`    | conjuctions (won vs. won't start)|

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: '-'
---
re.compile(
    r'(?:\#[\w\d]+\b)'
    r'|(?:\b\w[\/\&]\w)\b'
    r'|(?:\b\w[\w\'\d]+)\b'
).findall(
    "Stop H43; repos. to #5 grade."
    "Carburetor won't start."
)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Relational Pedantry: Graphs \& Ontologies

How we define and standardize known relations between entities. 

+++ {"slideshow": {"slide_type": "subslide"}}

Now that we have ways to _explicitly define_ what we intend an entity **occurence** to look like, we can start to _explicitly define_ the ways that entities relate to one-another. 

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

This is a (mathematical) _graph_, if we think of entities as **nodes** and relationships as **edges**

```{code-cell} ipython3
---
cell_style: split
hide_input: true
slideshow:
  slide_type: '-'
---
import graphviz
graphviz.Source(
    'digraph "entities and relations" '
    '{ rankdir=LR; '
    'A -> B [label="relation A:B"] '
    'C -> B [label="relation C:B"]'
    '}')
```

+++ {"slideshow": {"slide_type": "subslide"}}

There are many ways to use graphs to express how entities related to one another, but two of the most common are 


- **Labeled Property Graphs** e.g. NoSQL Graph Databases like [Neo4J](https://neo4j.com/), [JanusGraph](https://janusgraph.org/), etc.\
  Nodes and edges both have unique ID's, and can have internal properties (key-value).
- **Triple Stores** i.e. the Resource Description Framework ([RDF](https://www.w3.org/TR/rdf11-primer/))\
  All information is stored as triples: (subject, predicate, object). Every vertex has a unique identifier (no internal information). 

+++ {"slideshow": {"slide_type": "notes"}}

For more information comparing the two paradigms, see [this breakdown](https://neo4j.com/blog/rdf-triple-store-vs-labeled-property-graph-difference/) of a talk by Jesús Barrasa. We will return to these, and how knowledge engineering works (and interfaces with text data) more generally in later sections. 

LPG's come from a data-storage and querying community (think databases), while RDF comes from a web-technology culture (think W3C and Semantic Web). 
We will return to these later, but for now we want to focus on forms that _assumptions_ about entity relationships might take.  

+++ {"slideshow": {"slide_type": "subslide"}}

What kinds of relations are out there already? 

+++ {"slideshow": {"slide_type": "subslide"}}

### [WordNet](https://wordnet.princeton.edu/)

Lexical database for nouns, verbs, adverbs, and adjectives. 
- Groups terms into sets of synonyms (synsets) that have meaning
- Several types of relationships are available
    - Hyper/hyponyms (is-a). e.g. bed is a furniture
    - Mero/holonyms (part-of) e.g. bread part-of sandwich. 
    - entailment (implies) e.g. snore implies sleep. 
- Distinguishes between types (e.g. President) and instances (Abraham Lincoln)

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
import nltk
try:
    nltk.data.find('tokenizers/punkt')
    nltk.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('wordnet'); 
    nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn
wn.synsets('dog')
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
print(wn.synset('dog.n.01').definition())
print(wn.synset('dog.n.01').lemma_names())
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
# Hyper/Hyponyms
print('pasta could be: ', [i.lemma_names() for i in wn.synset('pasta.n.01').hyponyms()])
print('pasta is a: ', wn.synset('pasta.n.01').hypernyms())
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
# Holo/Meronyms
print('a living room is part of a: ', wn.synset('living_room.n.01').part_holonyms()[0].lemma_names())
```

```{code-cell} ipython3
---
hide_input: true
slideshow:
  slide_type: '-'
---
graphviz.Source('digraph {rankdir=LR '
                'living_room -> dwelling [label="part of"];'
                'dwelling -> home [label="same as"]'
                'dwelling -> abode [label="same as"]}')
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
[i.lemma_names() for i in wn.synset('car.n.01').part_meronyms()]
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Problem** \
WordNet is for _general english_, and is **not** exhaustive. 
If using for technical text, expect decent precision, but poor recall. 

```{code-cell} ipython3
:cell_style: center

[i.lemma_names() for i in wn.synset('bicycle.n.01').part_meronyms()]
```

+++ {"slideshow": {"slide_type": "fragment"}}

Meanwhile, from an engineering paper discussing bicycle drivetrains: 

```{code-cell} ipython3
---
cell_style: center
hide_input: true
slideshow:
  slide_type: '-'
---
graphviz.Source("""graph g { 
  graph[rankdir=LR, center=true, margin=0.2, nodesep=0.05, ranksep=0.1, bgcolor="transparent";];
  node[shape=plaintext, color=none, width=0.1, height=0.2, fontsize=11]
  pedal -- crank_arm;
  crank_arm -- chain_rings;
  chain_rings -- rear_derailleur;
  chain_rings -- chain;
  chain -- cogset;
  cogset -- rear_hub;
  rear_derailleur -- rear_hub;
  rear_hub -- rear_spokes;
  rear_spokes -- rear_rim;
  rear_rim -- rear_tire;
  
}
""")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
# Entailments
print('to buy means to: ', [i.lemma_names() for i in wn.synset('buy.v.01').entailments()])
print('to snore means to: ', [i.lemma_names() for i in wn.synset('snore.v.01').entailments()])
```

+++ {"slideshow": {"slide_type": "subslide"}}

For sources and more info: 
- https://www.nltk.org/howto/wordnet.html
- https://blog.xrds.acm.org/2017/07/power-wordnet-use-python/

+++ {"slideshow": {"slide_type": "subslide"}}

### ConceptNet

- **Crowdsourced knowledge**: Open Mind Common Sense, Wiktionary, DBPedia, Yahoo Japan / Kyoto University project
- **Games with a purpose**: Verbosity, nadya.jp
- **Expert resources**: Open Multilingual WordNet, JMDict, CEDict, OpenCyc, CLDR emoji definitions

Also uses _graph embeddings_ (we'll come back to this later) to "fuzzify" knowledge relationships. 

see: _ConceptNet in Context_, https://rcqa-ws.github.io/slides/robyn.pdf

+++ {"slideshow": {"slide_type": "subslide"}}

**How it works**:\
ConceptNet builds on WordNet and many others, using nodes and more generic "relations"
- PartOf, UsedFor, FormOf, HasA, CapableOf, Causes.... 
- see https://github.com/commonsense/conceptnet5/wiki/Relations

Interestingly, these are _not_ the "edges"... edges are assertions that have start and end-nodes, and _have a relation property_. 
- Edges can also have sources, weights (for uncertainty), licenses, datasets, "surfaceText" that generated the assertion, etc. 

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
import requests 

def conceptnet_query(q):
    url = 'http://api.conceptnet.io/'
    return requests.get(url+q).json()
conceptnet_query('c/en/bicycle?rel=/r/PartOf')
```

+++ {"slideshow": {"slide_type": "-"}}

Play around! see: https://conceptnet.io/c/en/bicycle?rel=/r/PartOf&limit=1000

+++ {"slideshow": {"slide_type": "slide"}}

## Takeaway


The "top-down" approach to transforming text into "something computable" is to express your intent as _rules_. 

**Entities** 
- "things that exist", and can have _types_ or _instances_. 
- we must map text occurences (tokens) to entities using rules e.g. RegEx

**Relationships** 
- how entities relate to each other, often as "verbs", but more generally as "predicates". 
- Will often see holonyms/meronyms, hypernyms/hyponyms, entailment, and synonyms
- How they are represented greatly depends on domain and historical use-case (database vs. web, etc.)

+++ {"slideshow": {"slide_type": "subslide"}}

We've only brushed the surface of ontologies and entity relationships, but the key point for this chapter is that _people had to write all of this down_! 
For rules-based systems, the name of the game is _human input_, which can be incredibly useful and powerful, while also being very fragile to context-specific application. 
It also takes _a lot of work_ to write down all of these rules, let alone validate them. 

Using one of these pre-existing rules-based systems is making, whether admitted or not, an _important assumption_ about the applicability of these rules to your problem!
