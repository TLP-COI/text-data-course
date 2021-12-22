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
import dvc.api as dvc
from pathlib import Path
import pandas as pd

import hvplot.pandas
import seaborn as sns
import pandera as pa

data_dir = Path(dvc.Repo().find_root())/'resources'/'data'/'mtg'
```

We've done some work to extract out a useful tabular form from the original (nested) json format. 

Validation is done using the following `pandera` schema:

```{code-cell}
# TODO: `AttributeError: module 'pandera' has no attribute 'io'`
# print(pa.io.from_yaml(data_dir/'mtg.schema.yaml'))
```

```{code-cell}
df = pd.read_feather(data_dir/'mtg.feather')
df.sample(10, random_state=2)
```

```{code-cell}
(df
 .set_index(df.release_date.astype('datetime64[ns]'))
#  .dropna(subset=['originalReleaseDate'])
 .sort_index()
 .resample('Y')
#  .text.apply(lambda s: s.str.contains('attack').sum())
 .apply(lambda grp: grp.flavor_text.notna().sum()/grp.shape[0])
#  .pipe(lambda g: g.sum()/g.size())
#  .transform
).hvplot( rot=45, title='What fraction of cards have Flavor Text?')

# (resample.sum()/(resample.size()+1)

# hvplot.converter.HoloViewsConverter(rot=45)
```
