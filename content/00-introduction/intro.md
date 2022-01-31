# Introduction

_The Road to Technical Language Processing_


```{sidebar} Text analysis?
```{mermaid}
graph LR
text --> ta(["text analysis?"])
style ta stroke-dasharray: 5 5
ta --> analyses
```

... profit?
```

Text Analysis can be hard to define.

It's often thought of as a "popular data mining technique": something that, tautologically, "text goes into" and "analyses" come out of. 


Less trivially, text analysis might be some set of "mutually agreed-upon" assumptions and patterns, all of which try to assist in _using_ text in computational or statistical ways.

```{sidebar} Once more, with feeling: 
```{mermaid} 
graph LR

assumptions --> ta(["text analysis?"])
style ta stroke-dasharray: 5 5
patterns --> ta
text --> results 
ta --> results
```
```

This is nothing to sneeze at. 
After all, using text ---especially _natural language_ text,  which can be full of symbolic and semantic meaning, written and intended _for_ humans to read and understand --- as a source of data? 

That is, arguably, _very cool_. 

Turning text, which seems to be almost certainly _subjective_ at some fundamental level, into something that _looks like objective data_, whether for decision support, investigations, understanding demographics, or question-answering, can absolutely feel magical. 

## Do you believe in Magic?
 

If we look at this definition again, though, "magical" can start to feel a bit _on the nose_...

```{mermaid}
:align: center
graph LR
subgraph magic
  assumptions --> ta(["text analysis?"])
  style ta stroke-dasharray: 5 5
  patterns --> ta
end
text --> results
ta --> results
```

````{margin} 
```{figure-md} xkcd-ml
![XKCD  Machine Learning](https://imgs.xkcd.com/comics/machine_learning.png)

And hey, it does eventually start looking "right", right? So what's the problem? 
(From Randall Munroe, [_XKCD_](https://xkcd.com/1838/))
```
````

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


````{margin} Black Box of Morgoth
```{figure-md} balrog
![Black Box of Morgoth](http://ackegard.com/gallery/d/5931-5/balrog.jpg)

An ethical data scientist fighting black-box NLP models on the bridge of Khazad-dum. 
(Image by Håkan Ackegård, from [Fantasy Gallery](http://ackegard.com/gallery/main.php))
```
````

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
All models are wrong; some are useful.

-- _every data scientist, all of the time_
```


The key is measuring and adjusting the model based on its _usefulness_.
I like to call engineering _"the art of applying science to solving people's problems"_.[^artofscience] 
I think this turn of phrase captures something important about using science to problem solve, whether that is building cities, designing cars, or doing data analysis for a policy firm: it's somewhat of an _artform_. 
There are many, _many_ subjective and context-sensitive decisions that _will get made_ throughout the entire process. 
But engineers, typically as positions of public trust, have developed systems, checks, and communities, that all overlap to try and mitigate the inherent risk in subjective decision-making.[^practicalengineer] 


[^artofscience]: I discovered a much more elegant version of this, recently. 
    From Jashree Seth's [award letter](https://alltogether.swe.org/2021/01/the-art-of-applying-science-to-life/) 
    to the Society of Women Engineers:
    
    > the art of applying science to life.

[^practicalengineer]: 
    [This video](https://www.youtube.com/watch?v=jxNM4DGBRMU) by Grady Hillhouse (_Practical Engineering_) is a succinct insight into this complex web of decisions and checks/balances that were _intended_ to prevent disaster, as well as the processes that kick into gear as soon as disaster occurs to understand _why_. 
    If you watch this video, pay attention to how many times subjective decisions were _necessary_, but also transparent enough that future instances could use this failure event as a solid case study. 
    As Grady says in the video description: 
    
    > Whether they realized it or not, the people living and working downstream of Oroville Dam put their trust in the engineers, operators, and regulators to keep them safe and sound against disaster. 
    > In this case, that trust was broken.

So we might say engineering is applying science, but 

> supplemented by necessary art [...] the know-how built up and handed down from past experience. 
> 
> [The know-how] is also called _engineering practice_. 
> In civil engineering, engineering practice refers to a body of knowledge, methods, and rules of thumb that consist of accepted techniques for solving problems and conducting business.
>
> The reason for the existence of this body of knowledge, engineering practice, is that engineers are accountable. 
> If a structure fails, the engineer is the one who is probably going to be held responsible.
> Nobody knows everything, and mistakes will happen despite the best preparation possible. 
> Engineers must show that they performed their duties according to the best of their abilities in accordance with accepted standards. 
> This is called performance. 
> The engineer's defense will be based on demonstrating that he or she followed acceptable engineering practice.
> 
> --- {cite:p}`hutcheson2003software`

```{margin}
Some reading this may think "of course not, those are _dangerous_ things, they _need_ all of that stuff!". 
I hope to cover some reasons that text analysis can be just as "dangerous" without proper oversight and critical thinking, in the case-studies chapter. 
```

Unfortunately, such "bodies of knowledge" and _practice_ are sorely lacking within data science and text analysis as it is in, say, building a dam, an aircraft, or a nuclear power plant. 
How does an analyst show they performed their duty according to their best ability? 
What _is_ "accepted text-as-data practice?"

```{admonition} Technical Language Processing (TLP) Community of Interest
:class: dropdown, tip
The TLP [community of interest](https://www.nist.gov/el/technical-language-processing-community-interest) is a group of researchers, academics, and industry professionals, largely from reliability engineering, that are trying to build and connect these "bodies of knowledge" to give analysts a better sense of accepted practice when applying text processing to technical domains. 
```

This is why I have organized this textbook with chapters named after steps of the "Engineering Approach". 
It is not an Engineering course, and you most definitely do not need to care about becoming an engineer to finish it. For the record, computer science has been applying engineering principles for a long time (thus the book reference used above).

Instead, these sections are meant to be an, admittedly unorthodox, way to introduce text analysis fundamentals in an application-centered way. 
Always remember _who_ might be trusting you with their data, their language, and their ear, when you analyse _text-as-data_. 

```{admonition} Steps in Practicing the _Engineering Approach_
:class: tip

- Goals & Approaches
  :  _"State the methods followed & why."_

- Assumptions
  :  _"State your assumptions._

- Measure & Evaluate 
  :  _"Apply adequate factors of safety."_

- Validate
  : _"Always get a second opinion"_

```

# References
```{bibliography}
:style: unsrtalpha
:filter: docname in docnames
```
