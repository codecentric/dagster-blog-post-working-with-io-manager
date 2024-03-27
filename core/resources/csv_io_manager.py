import pandas as pd
from dagster import UPathIOManager, InputContext, OutputContext
from upath import UPath

from core.resources.io_manager_factories import S3UPathIOManagerFactory


class CSVIOManager(UPathIOManager):
    def __init__(self):
        self.extension = ".csv"
        super().__init__()

    def load_from_path(self, context: InputContext, path: UPath) -> pd.DataFrame:
        with path.open("wb") as file:
            return pd.read_csv(file)

    def dump_to_path(self, context: OutputContext, obj: pd.DataFrame, path: UPath):
        with path.open("rb") as file:
            obj.to_csv(file, index=False)


class S3CSVIOManager(S3UPathIOManagerFactory):
    def io_manager_class(self):
        return CSVIOManager
