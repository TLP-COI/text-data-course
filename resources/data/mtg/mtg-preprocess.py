from pathlib import Path
import dvc.api as dvc
from tlp.data.mtg import loader, cleaner
import pandera as pa
import janitor as jn
# from tlp.data.utils import TLP_DATA_REPO
from tlp.data.mtg import MTG_DATA_PATH
# data_dir = Path(dvc.Repo().find_root()) / "resources" / "data" / "mtg")
if __name__ == "__main__":
    try:
        
        (
            loader()
            .also(lambda df: print("\nLoaded json, cleaning..."))
            .pipe(cleaner)
            .also(lambda df: print("\nSuccessfully cleaned MTG; saving as feather..."))
            .to_feather("mtg.feather")
        )
        print("\nMTG done!")
    except pa.errors.SchemaErrors as err:
        print("Schema errors and failure cases:")
        print(err.failure_cases)
        print("\nDataFrame object that failed validation:")
        print(err.data)
