# Expressions of Intent

In this "assumptions" component of practicing _text-as-data_, we are learning how one might choose represent text as  something _computable_ --- that is, assumptions that turn intractable problems into _feasibly tractable_ ones.
When dealing with computers as our tools in this quest, there are generally two ways of translating problems into something comput-_able_. The first way is the _rules-based_ method: 

Rules-based Methods
: - Prior-knowledge is encoded _explicitly_ as rules over patterns.
  - Behavior is acheived _implicitly_ through application of the rules to matched patterns. 

This "prior-knowledge" we encode are the "rules" part of "rules-based": we must write down what we want to happen, often on a case-by-case basis, as a series of _rules_. 

```{tip}
This Chapter's extra reading: 
- [Jurafsky, Ch. 2.1-4](https://web.stanford.edu/~jurafsky/slp3/2.pdf) and [Ch. 18.1-4,8](https://web.stanford.edu/~jurafsky/slp3/18.pdf)
- Julia Silge, [Introduction to _Tidy Text_]() 
```



We combine enough rules together, and observe behavior of our system in order to modify the rules, until the desired behavior is achieved (or, sufficiently approximated). 
If any of you played with Lego Mindstorms, or use `if-else` statements, you are familiar with writing rules for computer interpreters to follow. 
This chapter will scratch the surface of common uses for rules-based methods in extracting computationally-available information from text. 

The key challenge in writing rules-based methods is a balancing-act: be sufficiently _explicit_ enough to cover all the cases that need to have rules, while avoiding the _incredible_ labor-cost that can produce that kind of verbosity. 
Consequently there are many tools, communities, techniques, and theories to create, share, and apply rules-based methods to text. 
A lot of them involve the use of flexible creation of patterns or _expressions_ that can elegantly capture an analyst's _intent_. 

That's all we're really doing here: expressing our intent to a machine, as best as we are able. 
With that in mind, keep an eye out for these "pros" and "cons" in the rest of the chapter: 

```{admonition} Pros
:class: tip

- Typically **fast**: once written, applying rules can be likened to a look-up table. 
  > `if pattern: rule(pattern)`
  
  this scales quite well to huge amounts of text, and is optimized in modern languages. 

- **Transparency** and **Iteration**: writing rules will require that all analysts make positive affirmations of their beliefs and assumptions about the "world" they are working in. 
  This can make failure mitigation and stakeholder input _much_ more straight-forward. 

- **Robust**: once expressed, these rules are sometimes incredibly portable, and modular with other rules in similar domains. 
```

```{admonition} Cons
:class: warning

- **Labor-intensive**: generalizeable sets of rules will require a lot of human input, both in writing the rules, and in observing behavior to report back and/or _modify_ rules, accordingly. 
- **Fragile**: rules are typically _deeply_ embedded into a **context**. 
This means that application of these rules outside their context can have hidden and/or disasterous consequences. 
Especially true if their "modularity" led to novice use in a new domain. 

```