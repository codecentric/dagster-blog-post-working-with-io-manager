import pandas as pd

from core.resources.data_generator import DataGenerator


def test_generate_raw_training_data():
    data = DataGenerator().generate_raw_training_data()
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (100, 2)
    assert 'Feature' in data.columns
    assert 'Target' in data.columns
