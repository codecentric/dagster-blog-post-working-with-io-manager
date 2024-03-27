import tempfile
from os import path

import pandas as pd
from dagster import asset, materialize, AssetIn
from upath import UPath

from core.resources import PandasParquetIOManager


def test_pandas_parquet_io_manager():
    df_value = pd.DataFrame({
        "artists": ["Pet Shop Boys", "La Femme", "The Beatles"],
        "ratings": [9.5, 8.5, 7]
    })

    @asset(name='raw_data')
    def generate_data() -> pd.DataFrame:
        return df_value

    @asset(name="processed_data", ins={"raw_data": AssetIn()})
    def read_data(raw_data: pd.DataFrame) -> pd.DataFrame:
        return raw_data

    with tempfile.TemporaryDirectory() as temp_dir:
        res = materialize(
            assets=[
                generate_data,
                read_data,
            ],
            resources={
                "io_manager": PandasParquetIOManager(
                    base_path=UPath(temp_dir)
                ),
            },
        )

        assert res.success

        expected_files = [
            "raw_data.pq",
            "processed_data.pq",
        ]

        for file in expected_files:
            expected_path = path.join(temp_dir, file)
            assert path.exists(expected_path)
            intermediate_df = pd.read_parquet(expected_path)
            assert intermediate_df.equals(df_value)


