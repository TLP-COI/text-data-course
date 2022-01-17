# Introduction

_The Road to Technical Language Processing_


:::{sidebar} Text analysis?
```{mermaid}
graph TD
text --> ta(["text analysis?"])
style ta stroke-dasharray: 5 5
ta --> analyses
```

... profit?
:::

Text Analysis can be hard to define.

It's often thought of as a "popular data mining technique": something that, tautologically, "text goes into" and "analyses" come out of. 


Less trivially, text analysis might be some set of "mutually agreed-upon" assumptions and patterns, all of which try to assist in _using_ text in computational or statistical ways.

:::{sidebar} Once more, with feeling: 
```{mermaid} 
graph TD

assumptions --> ta(["text analysis?"])
style ta stroke-dasharray: 5 5
patterns --> ta
text --> comp["usable" computation/statistics]
ta --> comp
```
:::

This is nothing to sneeze at. 
After all, using text ---especially _natural language_ text,  which can be full of symbolic and semantic meaning, written and intended _for_ humans to read and understand --- as a source of data? 

That is, arguably, _very cool_. 

Turning text, which seems to be almost certainly _subjective_ at some fundamental level, into something that _looks like objective data_, whether for decision support, investigations, understanding demographics, or question-answering, can absolutely feel magical. 

## Do you believe in Magic?
 

If we look at this definition again, though, "magical" can start to feel a bit _on the nose_...

```{mermaid}
graph LR
subgraph magic
  assumptions --> ta(["text analysis?"])
  style ta stroke-dasharray: 5 5
  patterns --> ta
end
text --> comp["usable" computation/statistics]
ta --> comp
```

::::{margin} 
:::{figure-md} xkcd-ml
![XKCD  Machine Learning](https://imgs.xkcd.com/comics/machine_learning.png)

And hey, it does eventually start looking "right", right? So what's the problem? 
(From Randall Munroe, [_XKCD_](https://xkcd.com/1838/))
:::
::::

How do we know our assumptions (or anyone else's) are good? 
How do we know those assumptions _exist_, for that matter? 
Are the patterns "good"? 
Are the patterns relevant to the desired analysis? 

The pedantry seems a little pointless, surely... 

```{epigraph}
Obviously _someone_ has answered these questions, or why would text analysis be so popular? Can't I just use my _text as data_, already?

-- frustrated data scientists, probably
```

Unfortunately, things are not so straight-forward. 

Incentives for practitioners in the field of data science right now mean that there is often _very little_ reason to question the "magic", at least at first. 


::::{margin} Black Box of Morgoth
:::{figure-md} balrog
![Black Box of Morgoth](http://ackegard.com/gallery/d/5931-5/balrog.jpg)

An ethical data scientist fighting black-box NLP models on the bridge of Khazad-dum. 
(Image by Håkan Ackegård, from [Fantasy Gallery](http://ackegard.com/gallery/main.php))
:::
::::

Problems start arising when the outputs of these "analyses" have _impacts_. 
They might impact decisions, impact policymaking, impact _people's lives_. 
This tends to happen when technically-minded people, usually in need of more evidence to make better decisions (bless their heart!), start to turn to new "types" of data for answers. 
They might, for instance, turn to _text as data_. 

Our magical patterns and assumptions for dealing with text-as-data start to be used outside of their original context (e.g. from domains like linguistics or Natural Language Processing).
They get applied to technical domains like engineering, medicine, policy, threat assessment, risk modeling, actuarials, etc., all of which are built on the ethical application of evidence to serve others for the betterment of society.

>Despite recent dramatic successes, natural language processing (NLP) is not ready to address a variety of real-world problems. 
>Its reliance on large standard corpora, a training and evaluation paradigm that favors the learning of shallow heuristics, and large computational resource requirements, makes domain-specific application of even the most successful NLP techniques difficult.
>
> --- _{cite:t}`dimaadapting`_

Without asking those pedantic questions about assumptions and patterns, treating our text as "data" that _awoke in the darkness of ~~Khazad-dum~~ someone's NLP model_ will fundamentally contradict the purpose of those evidence-based fields.  




## A View from Engineering

All of this is not to say we _shouldn't use_ NLP or other text-analysis tools at all. 
They can be quite beneficial to us! 
The key is applying them critically and transparently. 

```{epigraph}
All models are wrong, some are useful

-- _every data scientist, all of the time_
```


:::{admonition} Engineering Practice
:class: tip

- Goals & Approaches
  :  _"State the methods followed & why."_

- Assumptions
  :  _"State your assumptions._

- Measure & Evaluate 
  :  _"Apply adequate factors of safety."_

- Validate
  : _"Always get a second opinion"_

:::

## Putting Things Together

View the use of _text-as-data_, and especially the application of NLP, as a **socio-technical system**, rather than as an algorithmic pipeline.



```{bibliography}
:style: unsrt
:filter: docname in docnames
```
