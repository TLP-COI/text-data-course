from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame as DF, Series as S, Index
import pandera.dtypes as d

try:
    from typing import Annotated  # python 3.9+
except ImportError:
    from typing_extensions import Annotated
# from pandera.io import from_yaml
import janitor as jn
import gzip, json
import toolz.curried as tz
from .utils import get_repository_datafolder


def loader(data_dir: Path) -> pd.DataFrame:
    with gzip.open(data_dir / "mtg.json.gz", "rt", encoding="UTF-8") as zipfile:
        df = tz.pipe(
            zipfile,
            json.load,
            tz.get("data"),
            ## First we have to get rid of {set-name-->{cards-->[]}} for {[{setname, cards-->[]}]}
            lambda d: d.items(),
            tz.map(lambda tup: tz.assoc(tup[1], "set", tup[0])),
            ## now normalize will be happy
            lambda d: pd.json_normalize(
                d,
                "cards",
                [  # keep some meta-data (set) lvl info
                    "code",
                    "releaseDate",
                    "block",
                ],
                errors="ignore",
            ),
        )
    return df


class MTGSchema(pa.SchemaModel):

    name: S[d.String]
    number: S[d.String]
    colors: S[object]  # list[str]
    color_identity: S[object]  # list[str]
    mana_cost: S[object] = pa.Field(nullable=True)  # list[str]
    converted_mana_cost: S[d.Float]
    power: S[d.Float] = pa.Field(nullable=True)
    toughness: S[d.Float] = pa.Field(nullable=True)
    life: S[d.Float] = pa.Field(nullable=True)
    text: S[pd.StringDtype]
    flavor_text: S[pd.StringDtype] = pa.Field(nullable=True)
    keywords: S[object] = pa.Field(nullable=True)  # list[str]
    code: S[d.String]
    release_date: S[d.DateTime]
    block: S[d.String] = pa.Field(nullable=True)
    edhrec_rank: S[d.Float] = pa.Field(nullable=True)
    rarity: S[Annotated[d.Category, ["rare", "common", "uncommon"], False]] = pa.Field(
        nullable=True
    )
    types: S[object]  # list[str]
    subtypes: S[object]  # list[str]
    supertypes: S[object]  # list[str]
    idx: Index[d.Int]

    class Config:
        coerce = True
        strict = "filter"


# @pa.check_output(MTGSchema.to_schema(), lazy=True)
def cleaner(df: pd.DataFrame) -> DF[MTGSchema]:
    return (
        df.clean_names(case_type="snake")
        .dropna(subset=["text"])
        .query('border_color=="black"')
        .reset_index()
        .transform_columns(
            ["power", "toughness", "life"],
            lambda s: pd.to_numeric(s, errors="coerce"),
        )
        .process_text(column_name="mana_cost", string_function="findall", pat=r"{(\w)}")
        .pipe(MTGSchema.validate, lazy=True)
    )


def manacost_symbols(s: pd.Series) -> pd.Series:
    from IPython.display import HTML

    HTML(
        '<link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.min.css" rel="stylesheet" type="text/css" />'
    )
    return s.fillna("").apply(
        lambda ls: "".join(
            ['<i class="ms ms-cost ms-{}"></i>'.format(i.lower()) for i in ls]
        )
    )


def style_table(df, hide_columns=None):
    """Display a dataframe with vertical column headers"""

    heading_style = {
        "selector": "th.col_heading",
        "props": [
            ("writing-mode", "sideways-lr"),
            ("vertical-align", "bottom"),
            ("transform-origin", "left"),
            ("transform", "rotate(45deg) translate(35px,-40px)"),
            ("border-bottom", "1px solid #ccc"),
        ],
    }

    cell_style = {
        #         'selector': 'th.col_heading',
        "selector": "td",
        "props": "text-align:left",
    }

    styles = [heading_style, cell_style]

    return (
        df.transform_columns(
            ["color_identity", "colors", "mana_cost"],
            manacost_symbols,
            elementwise=False,
        )
        .style.format(
            precision=0,
            formatter={
                "release_date": lambda x: x.strftime("%b '%y"),
            },
        )
        .hide_index()
        .hide_columns(hide_columns)
        .set_table_styles(styles, overwrite=False)
    )


def open_mtg() -> pd.DataFrame:
    mtg_folder = get_repository_datafolder() / "mtg"
    return pd.read_feather(mtg_folder / "mtg.feather")
