import dvc.api as dvc
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.io import from_yaml
import janitor as jn
import gzip, json
import toolz.curried as tz


data_dir = Path(dvc.Repo().find_root()) / "resources" / "data" / "mtg"
MTGSchema = from_yaml(data_dir / "mtg.schema.yaml")


def cleaner(df):
    return (
        df.clean_names(case_type="snake")
        .dropna(subset=["text"])
        .reset_index()
        .transform_columns(
            ["power", "toughness", "life"],
            lambda s: pd.to_numeric(s, errors="coerce"),
        )
    )


def loader(data_dir: Path) -> pa.typing.DataFrame[MTGSchema]:
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
                #             meta_prefix='_',
                errors="ignore",
            ),
            # now we clean up and validate using our schema
            cleaner,
            MTGSchema.validate,
        )
    return df


if __name__ == "__main__":

    loader(data_dir).to_feather(data_dir / "mtg.feather")
