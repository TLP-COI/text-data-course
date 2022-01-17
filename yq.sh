yq e -i '
    .dependencies |= . + [
      "poetry",
      "jupyter-book",
	  "jupytext",
	  "rise",
	  "nb_conda_kernels"
   ] |
   (.dependencies[] | select(tag=="!!map"))
   .pip |= . + [
      "sphinxcontrib-mermaid"
   ]
' env.yaml
