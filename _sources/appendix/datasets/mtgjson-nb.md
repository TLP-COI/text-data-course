---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# MTGJSON

> MTGJSON is an open-source project that catalogs all Magic: The Gathering cards in a portable format. A dedicated group of fans maintains and supplies data for a variety of projects and sites in the community. Using an aggregation process we fetch data between multiple resources and approved partners, and combine all this data in to various JSON files that you can learn about and download from this website.
>
> [mtgjson.com](mtgjson.com)

```{code-cell}
from frictionless import extract, Layout, Resource
import dvc.api as dvc
from pathlib import Path
import pandas as pd
import hvplot.pandas
```

```{code-cell}
# get_url('resources/data/mtg.csv')
# dvc.api.Repo().update()
data_fname = 'resources/data/mtg.csv'
rootdir = Path(dvc.Repo().find_root())
cards_layout = Layout(pick_fields=['name', 'text', 'flavorText', 'originalText','originalReleaseDate'])
df = Resource(rootdir/data_fname, layout=cards_layout).to_pandas()
```

```{code-cell}
df#[df.originalReleaseDate.notna()]
# Resource.to_pandas()
```

```{code-cell}
(df
 .originalReleaseDate
 .notna()  # is the original release date null?
 .value_counts()
 .to_frame().T.plot(kind='barh', stacked=True)
)
# df.plot()
```

```{code-cell}
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
