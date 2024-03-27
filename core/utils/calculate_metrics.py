import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def calculate_metrics(y_true, y_pred, X) -> pd.DataFrame:
    """
    Calculates MAE, MSE, RMSE, R-squared and Adjusted R-squared for the given true labels and predictions.

    Args:
    - y_true: The true target values.
    - y_pred: The predicted target values by the model.
    - X: The feature dataset used for the model training or prediction. Needed for Adjusted R-squared.

    Returns:
    - A Pandas DataFrame containing the calculated metrics.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r_squared = r2_score(y_true, y_pred)

    n = len(y_true)  # Number of observations
    p = X.shape[1]  # Number of features
    adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)

    metrics_df = pd.DataFrame({
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R-squared': r_squared,
        'Adjusted R-squared': adjusted_r_squared
    }, index=[0])

    return metrics_df
