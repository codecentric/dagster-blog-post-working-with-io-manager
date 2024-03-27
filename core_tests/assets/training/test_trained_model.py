import pandas as pd
from dagster import build_asset_context
from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_is_fitted

from core.assets.training.trained_model import train_model


def test_train_model():
    with build_asset_context() as context:
        train_data = pd.DataFrame({
            "Feature": [1, 2, 3, 4, 5],
            "Target": [2, 4, 6, 8, 10]
        })
        test_data = pd.DataFrame({
            "Feature": [6, 7, 8],
            "Target": [12, 14, 16]
        })

        model = train_model(context, train_data, test_data)
        assert isinstance(model, LinearRegression)
        check_is_fitted(model)