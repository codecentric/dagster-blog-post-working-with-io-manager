import pandas as pd
from dagster import asset, AssetIn, AssetExecutionContext
from sklearn.linear_model import LinearRegression

from core.utils.calculate_metrics import calculate_metrics


@asset(
    name="trained_model",
    io_manager_key="model_io_manager",
    ins={
        "train_data": AssetIn(),
        "test_data": AssetIn()
    },
)
def train_model(
        context: AssetExecutionContext,
        train_data: pd.DataFrame,
        test_data: pd.DataFrame,
) -> LinearRegression:
    """
    Train model with the training data subsets.
    """

    model = LinearRegression()
    model.fit(
        train_data[["Feature"]].to_numpy(),
        train_data[["Target"]].to_numpy()
    )

    y_pred = model.predict(test_data[["Feature"]].to_numpy())

    metrics = calculate_metrics(
        test_data[["Target"]].to_numpy(),
        y_pred,
        test_data
    )

    context.add_output_metadata(
        metrics.to_dict(orient='records')[0]
    )

    return model
