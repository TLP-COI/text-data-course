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

# MTGJSON

> MTGJSON is an open-source project that catalogs all Magic: The Gathering cards in a portable format. A dedicated group of fans maintains and supplies data for a variety of projects and sites in the community. Using an aggregation process we fetch data between multiple resources and approved partners, and combine all this data in to various JSON files that you can learn about and download from this website.
>
> [mtgjson.com](mtgjson.com)

```{code-cell} ipython3
import dvc.api as dvc
from pathlib import Path
import pandas as pd
from IPython.display import Code, HTML

import hvplot.pandas
import seaborn as sns
import pandera as pa

data_dir = Path(dvc.Repo().find_root())/'resources'/'data'/'mtg'
df = pd.read_feather(data_dir/'mtg.feather')
```

We've done some work to extract out a useful tabular form from the original (nested) json format. It is now stored as a `feather` file to speed up read-times. 

Validation is done using the following `pandera` schema:

```{code-cell} ipython3
from tlp.data import mtg, styleprops_longtext
from inspect import getsourcelines
Code(''.join(getsourcelines(mtg.MTGSchema)[0]), language='python')
```

There are key text columns that will be of use to this course, specifically, namely: 

name
: the name of the card

text
:  the rules-text displayed on the main "body" of the card-face. 

flavor-text
:  the "story" and "fantasy" bit, which may not always be present, and is usually prose. 

keywords
:  special, meaningful terms that appear in the "text", which have gameplay impacts

```{code-cell} ipython3
(df[['name', 'text','flavor_text']]
 .sample(10, random_state=2).fillna('').style
 .set_properties(**styleprops_longtext(['text','flavor_text']))
 .hide_index()
)
```

There are a number of other potential sources of "fortuitous data", as well:

+++

```{eval-rst}

.. raw:: html

    <link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.min.css" rel="stylesheet" type="text/css" />
    
```

```{code-cell} ipython3
%%HTML
<link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.min.css" rel="stylesheet" type="text/css" />
```

```{code-cell} ipython3
mtg.style_table(df.sample(10, random_state=2),
                        hide_columns=['text','flavor_text'])
```

```{margin}
All mana images and card symbols © Wizards of the Coast
The Mana font is licensed under the the SIL OFL 1.1
Mana CSS, LESS, and Sass files are licensed under the MIT License
```

Symbols are for vizualization only, with the original data consisting of lists of letters: `['W', 'U']`, etc. 
"Mana font" is made by [Andrew Gioia](https://mana.andrewgioia.com/index.html)

```{code-cell} ipython3
(df
 .set_index('release_date')
 .sort_index()
 .resample('Y')
 .apply(lambda grp: grp.flavor_text.notna().sum()/grp.shape[0])
).hvplot( rot=45, title='What fraction of cards have Flavor Text each year?')
```

```{code-cell} ipython3

```
