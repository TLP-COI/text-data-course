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
:::{margin}
On occaision, and especially during in-person lectures or labs, I will also use [Coconut](https://www.coconut-lang.org)
:::
Python has become somewhat of a "lingua franca" of the data science world, though other languages like R, Julia, or even MatLab are also widely used, loved, and powerful. 
Which you use will likely depend on the community you interact with most. 

With that aside, _managing_ Python as an interpreter and a set of libraries on your computer has historically been, shall we say... labarynthian? 

::::{sidebar} Enter the Labyrinth
:::{figure-md} xkcd-python
![XKCD Python Environment](https://imgs.xkcd.com/comics/python_environment.png)

Yes, things are actually _better_ now, than they used to be!
From Randall Munroe, [_XKCD_](https://xkcd.com/1987/)
:::
::::

How you approach the problem of dependency management for your projects depends on your community, and more specifically whether you lean toward _development_ of python tools (e.g. use [Poetry](https://python-poetry.org/)), or more toward _using_ those tools. 
In that case, which is what Data Science (and by extension, text analysis) falls under, the most common tool is `conda`. Either way, the key insight to both is liberal use of _environment isolation_. 

:::{hint} 
If that spaghetti in {numref}`xkcd-python` scares you, the trick is to keep everything separated by _what you want to DO with it_. 

_Remember: 1-environment-per-project!_
:::

If the words you are reading are not familiar, this is an excellent opportunity to check out the [Practical Data Science](https://www.practicaldatascience.org/html/setting_up_your_computer.html) guide to setting this up on your machine. 
I will not duplicate Nick's guide here, but I do have a few additional tips for this course (and years of trial-and-error). 

## (Ana?)Conda, but it's Mamba

:::{margin}
The default way to install `conda` in tutorials and lessons online will likely be the "full" or "large" installation from Anaconda, which contains a huge number of pre-installed packages from the `anaconda` channel. 
**I generally do not recommend this!**
Often it is much better to install the minimum and spin up environments with use-case specific packages/languages as needed. 
:::

First, terminology: 
- **Anaconda** is a data science corporation that develops a huge amount of open-source software, along with maintaining the "anaconda" repository channel of tools/packages that one could install using:
- `conda`, which is a program on your computer called a _package manager_, used through command-line. 
  Apart from installing libraries and versions of Python (or R or Julia or Haskell or [Coconut](https://www.coconut-lang.org), or many others), it will also help you to encapsulate these into isolated _conda environments_. 
- `mamba` is a recent re-implementation of `conda` that's [faster and has some nice features](https://mamba.readthedocs.io/en/latest/index.html). 


To keep your "base" conda environment clean (and running as fast as possible), look for a small installation like `miniconda`. 
A simple way to get `conda` installed with _minimal_ fluff, as well as a default channel with community-driven package curation, see the installable downlads on the  [`conda-forge/miniforge`](https://github.com/conda-forge/miniforge) page. 
Pick your OS and get going, _much faster than the old-days_!

## Modern Literate Programming with Jupyter

I remember the first time I encountered a so-called "notebook" for code, was in a calculus class with a professor absolutely _obsessed_ with [Mathematica](https://www.wolfram.com/mathematica/).
After using these new-fangled "cells" for my code and having results, comments, figures, and functions all interwoven togther in a beautiful tapestry for a semester, I became obsessed too. Alas, for I was but a poor student, and if I'm honest, unduly suspicious of licensed software. 

:::{margin}
Emacs gets a bad rap for its age and alternative binding schemes, but for the adventurous among you there are _modern_ distributions of emacs that become quite ergonomic and comfortable to use. 
You can even avoid the `vim`-vs-`emacs` holy war entirely by emulating vim-keybindings _inside_ emacs. 
Now both sides can hate you! 
See: [Doom](https://github.com/hlissner/doom-emacs) or [Spacemacs](https://www.spacemacs.org/) for some cool examples.
:::

This paradigm, of keeping your **code**, **story**, and **results** all interwoven in one file is typically called _literate programming_.
It's a powerful way to both explore your programming ideas, and document them as a cohesive narrative once better defined. 
Literate programming was championed by [Org-Mode](https://orgmode.org/) (an _extremely powerful_ plain-text system for note taking, authoring, and knowledge management built on `emacs`)
By the time I was discovering literate programming through Mathematica, the open source alternative I came accross was a fascinating web-browser stack built on the "python" language: IPython Notebooks. 

> Hacky? Yes.
> 
> Free and Open Source? You bet!

Today, that project has absolutely exploded into the de-facto method for data science experimentation, reporting, and communication, now called **Jupyter**.
Heck, this book is _written_ entirely using [ Jupyter(-book) ](https://jupyterbook.org/intro.html)!

:::{margin}
Jupyter, as an attempt to unify the statistical language communities, stood for **Ju**(lia)**Py**(thon)**R**. 
:::

:::{note}
Jupyter is a _server_-based coding interface. 
- Start a jupyter server: `jupyter lab` or `jupyter notebook`
- Access the running server through your browser: `localhos:8888`, or automatic
:::

A common misunderstanding: Jupter is _not_ "python", and using it isn't really dependent on your python installation above. 
Instead, the jupyter server frontend communicates with a programming language/interpreter _of your choosing_ through a jupyter _language kernel_. 
This architecture lets jupyter operate as a rich interface to [_many languages_](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels), not just python. 
That link has kernels to use anything from R and Julia to Haskell, Common Lisp, Clojure, MatLab, Ruby, or Fortran. 

In addition, being a web-first interface, Jupyter has a [huge number of extensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html), like adding scratchpads, widgets, bibtex citation support, and even live Reveal.js presentation mode through [RISE](https://rise.readthedocs.io/en/stable/), so you can live-demo _in style_!


## Version Veracity, Server Sanity, Kernel Correctness

:::{margin}
> _with great power, comes great responsibility..._
:::

In this course, I have adopted a few popular mechanisms to combat the proliferation of "junk notebooks".
Avoid addressing these problems at your peril! 

First, it is helpful to review this [guide to writing "Clean Notebooks"](https://ploomber.io/blog/clean-nbs/): 

> Notebooks are a magnificent tool to explore data, but such a powerful tool can become hard to manage quickly. 
> Ironically, the ability to interact with our data rapidly (modify code cells, run, and repeat) is the exact reason why a notebook may become an obscure entanglement of variables that are hard to understand, even to the notebook’s author.
> But it doesn’t have to be that way.
>
> --- Eduardo Blancas (2021)

:::{admonition} Keep your Notebooks _Clean_
:class: warning, dropdown
The freedom to mix code and notes in "cells" on a kernel-based web interface is _very_ easy to abuse. 
- Beware using lots of variable assignments. **Global State is the enemy.**
- Instead, capture reusable logic into **functions**, save them in **source files**, and **apply** them in the notebook all at once. 
- Keep notebooks short and focused. Import functions+data, tell your story, make your point, end-of-notebook. New notebooks are free, so use them!
- The `.ipynb` file format is not human-friendly or easy to diff in version-control... more of a json/hashstring/_mess_, needing the frontend to interpret. _Plain-text is your friend!_
:::

:::{margin}
This textbook repository uses [Poetry](http://www.python-poetry.org) to create installable source code for notebooks to import.
:::

I don't follow everything in this post exactly (for instance, I typically use `pyproject.toml` over `setup.py` to make source-code files for python functions/types, based on the now-standard PEP 518). 
But the advice is generally good and well worth a read-through. 

Additional tools used for this book to help you stay sane in the wonderful journey to productive notebook use are below. 

### [Jupytext](https://jupytext.readthedocs.io/en/latest/)

Creates and syncs `.md` files (or, script files for each kernel's language) that can roundtrip to/from `.ipynb` files. This lets you add `*.ipynb` to your `.gitignore` (see [DevOps](tools-02ops.md)) and never deal with unmergeable diff files again. Also great for collaboration, since your colleague only needs to edit a plain text file (e.g. on GitHub) and you will recieve a fresh, edited notebook, locally.

### YAML Environment specifications
Remember:

> _1-environment-per-project!_

So, you will have a lot of environments running around, with you and collaborators needing to add or remove dependencies, constantly. 
If only there was a way to make some kind of _recipe_ file, that could read a list of things you want, and then "update" the environment whenever you want...

:::{margin}
Personally, I add `.conda_env_base.yml` and `.conda_env_notebooks.yml` to my [_dotfiles_ repository](https://gitlab.com/tbsexton/dotfiles) so every computer can have the same setup, automatically! 
:::

In case you didn't see this in the mountain of conda documentation, [this exists](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually), and should probably be the _only way_ you make environments. 

These `environment.yaml` files are incredibly powerful, and _will save you time and sanity working with other people_. 

:::{admonition} Example `environment.yaml`
:class: tip, dropdown

Here's an example file that governs a conda/mamba environment named `test`:

```yaml
name: test
channels: 
  # This is where stuff gets downloaded from
  - conda-forge
  - pyviz

dependencies:
  - python=3.9  # can lock version numbers
  - ipykernel  # needed to use "python" from a notebook
#  - irkernel  # could've been "R"
  - pandas
  - panel  # comes from the pyviz channel
  - pip  # ALWAYS INSTALL PIP if you want to use `pip install` inside the environment!
  - pip:  # now we can tell `pip` to install its own package list automatically
    - textacy
    # - -e .  # if we wanted to install local directory (e.g. pyproject.toml/setup.py)
    # - frictionless[json]  # can use standard pip syntax for e.g. options

```

In the directory containing this file, say, `test-env.yml`, you would create/update the environment `test` with the command:

```bash
conda env update -f test-env.yml
```

Now is a good time to try making your own environment for this course... see if you can make a `text-data-env.yml` on your own!


:::

### [`nb_conda_kernels`](https://github.com/Anaconda-Platform/nb_conda_kernels)

However, due to being largely implemented _in python_, the Jupyter server is installed into a base environment, and has no idea about other environments while running. 
In practice, this means everyone ends up re-installing Jupyter into every project's environment, which is both 

1. wasteful of space, and memory, and terminal tabs (running _many_ instances of jupyter at once)
2. loses any extensions/custom settings you might have had in another environment. 

Instead, the folks at Anaconda have created a (temporary) fix for this hell: `nb_conda_kernels`. 
This extension gets installed _once_, alongside a single installation of `jupyter` (e.g. in `base` or a custom `notebooks` environment). 
Then, any time you create an environment with a valid language kernel (`ipykernel`, `irkernel`, `coconut[kernel]`, etc. ), you will see that kernel and be able to run _any_ notebook inside its corresponding environment. 
Switch between kernels from inside the notebook with `Kernel > Change kernel`

_Feels good, man._





