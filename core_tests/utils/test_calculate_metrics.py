import pandas as pd

from core.utils.calculate_metrics import calculate_metrics


def test_calculate_metrics():
    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    X = pd.DataFrame({
        'feature1': [1, 2, 3, 4],
        'feature2': [5, 6, 7, 8]
    })

    metrics_df = calculate_metrics(y_true, y_pred, X)

    expected_metrics = pd.DataFrame({
        'MAE': 0.5,
        'MSE': 0.375,
        'RMSE': 0.612372,
        'R-squared': 0.948608,
        'Adjusted R-squared': 0.845824,
    }, index=[0])

    pd.testing.assert_frame_equal(metrics_df, expected_metrics)
