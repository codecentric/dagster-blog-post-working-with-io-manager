from dagster import asset

from core.resources.data_generator import DataGenerator


@asset(name="preprocessed_data")
def preprocess_data(data_generator: DataGenerator):
    """
    Process raw training data.
    """
    raw_data = data_generator.generate_raw_training_data()

    # do "something" with raw_data

    return raw_data
