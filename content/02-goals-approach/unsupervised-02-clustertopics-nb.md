---
jupytext:
  formats: ipynb,md:myst
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

```{code-cell} ipython3
%load_ext coconut
```

```{code-cell} ipython3
import re
import numpy as np
rng = np.random.default_rng(2)
import pandas as pd
import janitor as pj
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import seaborn as sns
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
from bokeh.models import HoverTool
from holoviews.operation.datashader import datashade, dynspread, rasterize
import datashader as ds


# tooltips = [
#     ('Text', '@text'),
#     ('Flavor', '@flavor_text'),
#     ('Color ID','@color_identity'),
#     ('Cluster', '@cluster')
# ]
color_mapping = {'W': 'tan', 'U': 'blue', 'B': 'purple', 'R': 'red', 'G': 'green', 'M': 'goldenrod'}
mana_color_dim = hv.dim('color_identity').categorize(color_mapping, default='grey')
fullwidth=dict(height=450, width=900)
# hover = HoverTool(tooltips=tooltips)
opts.defaults(opts.Scatter(tools=['hover'], size=8, **fullwidth), 
              opts.Points(tools=['hover'], size=8, **fullwidth))
```

+++ {"slideshow": {"slide_type": "skip"}}

# Let Simmer, Unsupervised

```{code-cell} ipython3
%%coconut 
from tlp.data import DataLoader

df = (
    DataLoader.mtg()
    .dropna(subset=['flavor_text', 'text'])
#     .fillna(value={'color_identity':'NA'})
    .transform_column('color_identity', s->''.join(set(s)),elementwise=True)
    .replace(to_replace={'color_identity':re.compile('\w{2,}')}, value='M')
)
text = df.text.str.cat(others=[df.name, df.flavor_text], sep='\n')#.fillna('')
df.head()
```

```{code-cell} ipython3
# from syntok.tokenizer import Tokenizer

# tok = Tokenizer()  # optional: keep "n't" contractions and "-", "_" inside words as tokens
# text.apply(list..(tok.tokenize))

import re
tokenize = re.compile(
    r'(?:\#[\w\d]+\b)'
    r'|(?:\b\w[\/\&]\w)\b'
    r'|(?:\b\w[\w\'\d]+)\b'
    r'|(?:\{\w\})'  # mana
    r'|(?:[+-]\d\d?(?:/[+-]\d\d?)?)'  # tokens
)

text.str.findall(tokenize).explode().unique()[:100]
```

## Visualize

```{code-cell} ipython3
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
import umap, umap.plot
from sklearn.decomposition import TruncatedSVD

vsm = TfidfVectorizer(
    tokenizer=tokenize.findall,
    min_df=3, 
    max_df=0.8,
    stop_words='english',
    ngram_range=(1,2),
)  # vector-space model
manifold = Pipeline([
    ('pca',TruncatedSVD(n_components=100)),
    ('tsne', TSNE(learning_rate='auto', init='random'))
])
# manifold = umap.UMAP(n_components=2, metric='cosine', n_neighbors=15)

sample = rng.choice([True, False], size=len(text), p=[0.2, 0.8])
```

```{code-cell} ipython3
X = vsm.fit_transform(text)
X_2d = manifold.fit_transform(X[sample,:])

X_2d.shape
```

```{code-cell} ipython3
# df_samp = 

key_dimensions = [('x', 'Dim-1'), ('y', 'Dim-2')]
value_dimensions = [
    ('text', 'Rules Text'), 
    ('flavor_text', 'Flavor Text'), 
    ('color_identity', 'Color ID'),
]
macro = hv.Table(df[sample].assign(x=X_2d[:,0], y=X_2d[:,1]), key_dimensions, value_dimensions)
macro.to.points(['x','y'])
```

```{code-cell} ipython3
%%coconut
scatter = (macro.to.points(['x','y'], groupby='color_identity')
 .overlay()
#  .opts(**fullwidth)
#  |> datashade$(aggregator=ds.by('color_identity', ds.count()))
#  |> dynspread
 |> .opts(opts.Points(color=mana_color_dim, tools=['hover', 'lasso_select'], **fullwidth))
)
scatter
```

```{code-cell} ipython3
macro.to.points(['x','y'], groupby='color_identity').opts(opts.Points(width=600, color=mana_color_dim))
```

## Keywords

```{code-cell} ipython3
pd.Series(
    np.asarray(X.sum(axis=0))[0], 
    index=vsm.get_feature_names_out()
).sort_values(ascending=False).head(40)
```

```{code-cell} ipython3

```

## Clustering

```{code-cell} ipython3
%%coconut
import hdbscan
clust = hdbscan.HDBSCAN(
#     min_samples=1,
#     min_cluster_size=30,
    metric='cosine',
)
highD_labels = clust.fit_predict(X[sample,:]) |> pd.Series
clust.condensed_tree_.plot()
```

```{code-cell} ipython3
highD_labels.value_counts()
```

```{code-cell} ipython3
# scatt2 = hv.Scatter(df_samp.assign(cluster=highD_labels.values),'x', 
#            vdims=['y', 'text', 'flavor_text', 'cluster']).opts(color='cluster', cmap='glasbey', size=5)
# scatt2
macro.add_dimension('cluster', 0, highD_labels.values).to.points(['x','y'], groupby='cluster').overlay()
```

```{code-cell} ipython3
## from docs: https://umap-learn.readthedocs.io/en/latest/clustering.html
# clusterable_embedding = umap.UMAP(
#     n_neighbors=40,
#     min_dist=0.1,
#     n_components=2,
#     random_state=42,
# ).fit_transform(vsm.transform(text[sample]))
```

```{code-cell} ipython3
%%coconut
clust =hdbscan.HDBSCAN(
#     min_samples=10,
    min_cluster_size=10,
    cluster_selection_epsilon=2,
)
labels=clust.fit_predict(X_2d)|> pd.Series #|> .replace(-1, None)
clust.condensed_tree_.plot()
```

```{code-cell} ipython3
labels.value_counts()
```

```{code-cell} ipython3
# hdbscan.all_points_membership_vectors(clust)

macro.add_dimension('cluster', 0, labels.values).to.points(['x','y'], groupby='cluster').overlay()
```

### Cheating?

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
---
%%coconut
from sklearn.preprocessing import LabelEncoder

class_encode = LabelEncoder()
targets = class_encode.fit_transform(df.loc[sample, 'color_identity'].values)
metric_learn = umap.UMAP(target_metric='categorical', target_weight=0.3)

M_2d = (
    text[sample] 
    |> vsm.transform 
    |> metric_learn.fit_transform$(y=targets)
)
```

```{code-cell} ipython3
new_macro = (
    macro
    .add_dimension('x-class',0, M_2d[:,0])
    .add_dimension('y-class',1, M_2d[:,1])
)
(new_macro.to.points(['x-class','y-class'], groupby='color_identity')
 .overlay().opts(opts.Scatter(cmap=color_mapping))
#  |> datashade$(aggregator=ds.by('color_identity', ds.count()))
#  |> dynspread
#  |> .opts(**fullwidth)
)
```

## Topic Modeling

+++

### Latent Semantic Indexing (i.e. SVD)

```{code-cell} ipython3
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()

    
plot_top_words(
    TruncatedSVD(n_components=10).fit(X), vsm.get_feature_names_out(), 10, "Topics (Frobenius norm)"
)
```

### Non-Negative Matrix Factorization (NMF)

```{code-cell} ipython3
from sklearn.decomposition import NMF, LatentDirichletAllocation

topics = NMF(n_components=10)
topics.fit_transform(X)
```

```{code-cell} ipython3
plot_top_words(
    topics, vsm.get_feature_names_out(), 10, "Topics (Frobenius norm)"
)
```

### Latent Dirichlet Allocation

```{code-cell} ipython3
topics = LatentDirichletAllocation(n_components=30)
topics.fit_transform(X)
    
plot_top_words(
    topics, vsm.get_feature_names_out(), 10, "Topics (Frobenius norm)"
)
```
