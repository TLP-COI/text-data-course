# Setting up a Computing Environment

_Opinionated, (hopefully) sane, defaults to build on_

:::{admonition} TL;DR
:class: tip, dropdown

1. read background: 
   - [Setting up your computer](https://www.practicaldatascience.org/html/setting_up_your_computer.html) by Practical Data Science
   - [On writing clean Jupyter notebooks](https://ploomber.io/blog/clean-nbs/)
2. download and install [`conda-forge/miniforge`](https://github.com/conda-forge/miniforge)
3. In a `base` or `notebooks` environment, install Jupyter (notebook or lab), along with `jupytext` and other extensions
4. Install `nb_conda_kernels` alongside the notebook server, letting it access other kernels. Remember, 1-environment-per-project!
5. Use `environment.yaml` spec files to track and share your dependencies for each environment/project. 
6. Don't forget to list a kernel for the language(s) you want to use in the `environment.yaml`, such as `ipykernel`, `irkernel`, `coconut[kernel]`, etc.

:::

The material in this course is written primarily using Python. 
Python has become somewhat of a "lingua franca" of the data science world, though other languages like R, Julia, or even MatLab are also widely used, loved, and powerful. 
Which you use will likely depend on the community you interact with most. 

With that aside, _managing_ Python as an interpreter and a set of libraries on your computer has historically been, shall we say... labarynthian? 

:::{figure-md} xkcd-python
![XKCD Python Environment](https://imgs.xkcd.com/comics/python_environment.png)

Yes, things are actually _better_ now, than they used to be!
From Randall Munroe, [_XKCD_](https://xkcd.com/1987/)
:::

How you approach the problem of dependency management for your projects depends on your community, and more specifically whether you lean toward _development_ of python tools (e.g. use [Poetry](https://python-poetry.org/)), or more toward _using_ those tools. 
In that case, which is what Data Science (and by extension, text analysis) falls under, the most common tool is `conda`. Either way, the key insight to both is liberal use of _environment isolation_. 

:::{hint} 
If that spaghetti in {numref}`xkcd-python` scares you, the trick is to keep everything separated by _what you want to DO with it_. 

_Remember: 1-environment-per-project!_
:::

If the words you are reading are not familiar, this is an excellent opportunity to check out the [Practical Data Science](https://www.practicaldatascience.org/html/setting_up_your_computer.html) guide to setting this up on your machine. 
I will not duplicate Nick's guide here, but I do have a few additional tips for this course (and years of trial-and-error). 

## (Ana?)Conda, but it's Mamba

First, terminology: 
- **Anaconda** is a data science corporation that develops a huge amount of open-source software, along with maintaining the "anaconda" repository channel of tools/packages that one could install using:
- `conda`, which is a program on your computer called a _package manager_, used through command-line. 
  Apart from installing libraries and versions of Python (or R or Julia or Haskell or many others), it will also help you to encapsulate these into isolated _conda environments_. 
- `mamba` is a recent re-implementation of `conda` that's faster and has some nice features. 

:::{note}
The default way to install `conda` in tutorials and lessons online will likely be the "full" or "large" installation from Anaconda, which contains a huge number of pre-installed packages from the `anaconda` channel. 
**I generally do not recommend this!**
:::

To keep your "base" conda environment clean (and running as fast as possible), look for a small installation like `miniconda`. 
A simple way to get `conda` installed with _minimal_ fluff, as well as a default channel with community-driven package curation, see the installable downlads on the  [`conda-forge/miniforge`](https://github.com/conda-forge/miniforge) page. 
Pick your OS and get going, _much faster than the old-days_!

## Modern Literate Programming with Jupyter

I remember the first time I encountered a so-called "notebook" for code, was in a calculus class with a professor absolutely _obsessed_ with [Mathematica](https://www.wolfram.com/mathematica/).
After using these new-fangled "cells" for my code and having results, comments, figures, and functions all interwoven togther in a beautifu tapestry for a semester, I became obsessed too. Alas, for I was but a poor student, and if I'm honest, unduly suspicious of licensed software. 

At the time, I came accross this fascinating alternative built on a web-browser stack and the "python" language I had been trying out, called IPython Notebooks. 

> Hacky? Yes.
> 
> Free and Open Source? You bet!

Today, that project has absolutely exploded into the de-facto method for data science experimentation, reporting, and communication, now called Jupyter.
Heck, this book is _written_ entirely using [ Jupyter(-book) ](https://jupyterbook.org/intro.html)!

:::{margin}
Jupyter, as an attempt to unify the statistical language communities, stood for **Ju**(lia)**Py**(thon)**R**. 
:::

Jupyter `{lab|notebook}`

- 
- Clean NB's
- project structure, installables

## Server Sanity, Kernel Correctness

- `nb_conda_kernels`
- yaml env spec's


