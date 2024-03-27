import pandas as pd

from core.assets.preprocessing.split_data import split_data
from core.configs import SplitDataConfig


def test_split_data():
    config = SplitDataConfig(test_size=0.2, random_state=42)
    preprocessed_data = pd.DataFrame({
        'Feature': [1, 2, 3, 4, 5],
        'Target': [2, 4, 6, 8, 10]
    })

    expected_train_data = pd.DataFrame({
        'Feature': [5, 3, 1, 4],
        'Target': [10, 6, 2, 8]
    })

    expected_test_data = pd.DataFrame({
        'Feature': [2],
        'Target': [4]
    })

    train_data, test_data = split_data(config, preprocessed_data)

    assert train_data.shape == (4, 2)
    assert test_data.shape == (1, 2)

    pd.testing.assert_frame_equal(train_data.reset_index(drop=True), expected_train_data)
    pd.testing.assert_frame_equal(test_data.reset_index(drop=True), expected_test_data)
