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

# "Tiny" Shakespeare

As made popular by Andrej Karpathy in his [blog post *The Unreasonable Effectiveness of RNN's*](https://karpathy.github.io/2015/05/21/rnn-effectiveness/), this selection from several of Shakespeare's works has seen re-use in various tutorials, librarys, demos, including Tensorflow and HuggingFace, themselves.

```{code-cell}
from pathlib import Path
import dvc.api as dvc

data_dir = Path(dvc.Repo().find_root())/'resources'/'data'/'shakespeare'/'shakespeare.txt'
```

```{code-cell}
# Get raw text as string.
text = data_dir.read_text()

print(text[1000:1500])
```

## Markov Language Model

```{code-cell}
import markovify
model = markovify.Text(text, state_size=2, well_formed=False)
model.make_sentence(tries=500)
```

```{code-cell}
for i in range(5):
    print(model.make_sentence_with_start('Therefore, we', strict=False, tries=500))
```

```{code-cell}

```

```{code-cell}

```
