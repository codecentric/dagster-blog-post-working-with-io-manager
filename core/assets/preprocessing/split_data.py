import pandas as pd
from dagster import AssetIn, multi_asset, AssetOut
from sklearn.model_selection import train_test_split

from core.configs import SplitDataConfig


@multi_asset(
    ins={
        "preprocessed_data": AssetIn()
    },
    outs={
        "train_data": AssetOut(io_manager_key="parquet_io_manager"),
        "test_data": AssetOut(io_manager_key="parquet_io_manager"),
    }
)
def split_data(config: SplitDataConfig,
               preprocessed_data: pd.DataFrame):
    """
    Split data into subsets
    """
    X = preprocessed_data[['Feature']]
    y = preprocessed_data['Target']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
    )

    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)

    return train_data, test_data
