from dagster import Config
from pydantic import Field


class SplitDataConfig(Config):
    test_size: float = Field(description="Proportion of the dataset to include in the test split.", default=0.2)
    random_state: int = Field(description="Seed for data shuffling.", default=42)
