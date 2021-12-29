from pathlib import Path
import dvc.api as dvc
from tlp.data.mtg import loader, cleaner
import pandera as pa
import janitor as jn

data_dir = Path(dvc.Repo().find_root()) / "resources" / "data" / "mtg"

if __name__ == "__main__":
    try:
        (
            loader(data_dir)
            .also(lambda df: print("\nLoaded json, cleaning..."))
            .pipe(cleaner)
            .also(lambda df: print("\nSuccessfully cleaned MTG; saving as feather..."))
            .to_feather(data_dir / "mtg.feather")
        )
        print("\nMTG done!")
    except pa.errors.SchemaErrors as err:
        print("Schema errors and failure cases:")
        print(err.failure_cases)
        print("\nDataFrame object that failed validation:")
        print(err.data)
