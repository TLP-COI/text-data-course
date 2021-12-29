def styleprops_longtext(columns: list[str] = None):
    """display long dataframe text nicer.

    For use in `pandas.io.formats.style.Styler.set_properties`:

    ```python
    df.style.set_properties(**styleprops_longtext( ['text-col-1', 'text-col-2'] ))
    ```

    By default, this shrinks , left-aligns, and word-wraps text, limiting width to 250px
    """

    return {
        "subset": columns,
        "word-wrap": "normal",
        "text-align": "left",
        "font-style": "italic",
        "font-size": "0.8em",
        "width": "250px",
    }
