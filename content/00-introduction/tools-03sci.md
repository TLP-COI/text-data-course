# Tools for Data Science

So far in this (over-long) introduction, we've introduced the ways that technical communities find their heading (e.g. _engineering practice_), and why roads are important to go, efficiently, in that direction (e.g. data-driven fields need _data infrastructure_). 
The last thing we need for this metaphor are vehicles to get us to our destination: domain-specific tools (methods, algorithms, frameworks, etc.). 

To keep things interesting, key tools will be introduced in the context of their _use_, from here-on-out. 
Rather than go into great detail, then, this page will store a maintained table of tools, with any [notes on their use]() shortly after.  

## Tables, Vectors, & Graphs
Basic ways of representing and manipulating data. 

```{list-table}
:header-rows: 1
:name: tools-data

* - Tool Name
  - Description
  - Docs/Tutorials
  - `R` option
  - Notes
* - Numpy/Scipy
  - matrix (dense or sparse) manipulation and routines
  - [quickstart](https://numpy.org/doc/stable/user/quickstart.html) 
  - `matrix`
  - 
* - Pandas
  - All-purpose tabular data loader, manipulator, and writer. 
  - [docs]()
  - `data.frame`
  - [Important! See below](notes:pandas)
* - pyJanitor
  - Convenient methods to (sanely) clean up your data-frame, in-line
  - 
  - 
  - 
* - XArray
  - N-dimensional extension of Pandas' "named arrays", based on NetCDF 
  - [docs](https://xarray.pydata.org/en/stable/index.html)
  - [`tidync`](https://docs.ropensci.org/tidync/)
  - 
* - NetworkX
  - Graphs (vertices+edges) as general-purpose dictionaries with methods. 
  - []
  - [`tidygraph`]()
  - 
* - graph-tool
  - C-based network analysis, focused on stochastic block models. 
  - []
  - 
  - 
```

## Machine Learning
```{list-table}
:header-rows: 1
:name: tools-ml

* - Tool Name
  - Description
  - Docs/Tutorials
  - `R` option
  - Notes
* - Scikit-Learn
  - Standard for ML in Python
  - [Scikit-Learn Course](https://inria.github.io/scikit-learn-mooc/index.html#)
  - 
  - 

```


## Natural Language Processing
```{list-table}
:header-rows: 1
:name: tools-nlp

* - Tool Name
  - Description
  - Docs/Tutorials
  - `R` option
  - Notes
* - NLTK
  - 
  - 
  - 
  - 
* - Spacy/Textacy
  - 
  - 
  - 
  - 
* - Gensim
  - 
  - 
  - 
  - 
* - flair
  - 
  - 
  - 
  - 
* - huggingface
  - 
  - 
  - 
  - 
* - cleantext
  - 
  - 
  - 
  - 
  
```


## Visualization
```{list-table}
:header-rows: 1
:name: tools-viz

* - Tool Name
  - Description
  - Docs/Tutorials
  - `R` option
  - Notes
* - matplotlib.pyplot
  - 
  - 
  - 
  - 
* - seaborn
  - 
  - 
  - 
  - 
* - pyviz
  - 
  - 
  - 
  - [see below]()
```



## Notes

(notes:pandas)=
### Pandas
For an excellent series on using pandas more effectively (which we _all_ need to do), see this fantastic series from Tom Augsperger: [Modern Pandas](https://tomaugspurger.github.io/modern-1-intro). 
For this course, ensure you read the [method chaining](https://tomaugspurger.github.io/method-chaining.html) post! 
It will dramitically alter (read: enhance) your code quality and maintainability while using pandas for data munging. 

### Jax

### Pyviz

