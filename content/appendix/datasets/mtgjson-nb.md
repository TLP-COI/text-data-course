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
from frictionless import extract, Layout, Resource
import dvc.api as dvc
from pathlib import Path
import pandas as pd
import hvplot.pandas
```

```{code-cell} ipython3
# get_url('resources/data/mtg.csv')
# dvc.api.Repo().update()
data_fname = 'resources/data/mtg.csv'
rootdir = Path(dvc.Repo().find_root())


with dvc.open(data_fname) as csv:
    df = pd.read_csv(csv, index_col=0)#.fillna('')

# cards_layout = Layout(pick_fields=['name', 'text', 'flavorText', 'originalText','originalReleaseDate'])
# df = Resource(df, layout=cards_layout).to_pandas()
```

```{code-cell} ipython3
df#[df.originalReleaseDate.notna()]
# Resource.to_pandas()
```

```{code-cell} ipython3
(df
 .originalReleaseDate
 .notna()  # is the original release date null?
 .value_counts()
 .to_frame().T.plot(kind='barh', stacked=True)
)
# df.plot()
```

```{code-cell} ipython3
resample = (df
 .set_index(df.originalReleaseDate.astype('datetime64[ns]'))
 .dropna(subset=['originalReleaseDate'])
 .sort_index()
 
 .text.str.contains('tap')
 .resample('Y')
)

(resample.sum()/(resample.count()+1)
).hvplot(kind='step', rot=45)
# hvplot.converter.HoloViewsConverter(rot=45)
```
