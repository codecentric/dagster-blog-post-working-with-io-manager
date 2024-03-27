from typing import Any

import joblib
from dagster import InputContext, OutputContext, UPathIOManager
from upath import UPath

from core.resources import S3UPathIOManagerFactory


class ModelIOManager(UPathIOManager):
    extension: str = ".pickle"

    def dump_to_path(self, context: OutputContext, obj: Any, path: UPath):
        with path.open("wb") as file:
            joblib.dump(obj, file)

    def load_from_path(self, context: InputContext, path: UPath) -> Any:
        with path.open("rb") as file:
            return joblib.load(file)


class S3ModelIOManager(S3UPathIOManagerFactory):
    def io_manager_class(self):
        return ModelIOManager
