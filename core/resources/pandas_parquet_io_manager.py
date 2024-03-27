from typing import Type

import pandas as pd
from dagster import UPathIOManager, OutputContext, InputContext
from upath import UPath

from core.resources.io_manager_factories import S3UPathIOManagerFactory


class PandasParquetIOManager(UPathIOManager):
    extension: str = ".pq"

    def dump_to_path(self, context: OutputContext, obj: pd.DataFrame, path: UPath):
        context.add_output_metadata({
            "row_count": len(obj)
        })

        with path.open("wb") as file:
            obj.to_parquet(file)

    def load_from_path(self, context: InputContext, path: UPath) -> pd.DataFrame:
        with path.open("rb") as file:
            return pd.read_parquet(file)


class S3PandasParquetIOManager(S3UPathIOManagerFactory):
    def io_manager_class(self) -> Type[PandasParquetIOManager]:
        return PandasParquetIOManager
