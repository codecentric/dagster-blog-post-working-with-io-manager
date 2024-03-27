import numpy as np
import pandas as pd
from dagster import ConfigurableResource
from pydantic import Field


class DataGenerator(ConfigurableResource):
    size: int = Field(description="Size of the generated dataset", default=100)

    def generate_raw_training_data(self) -> pd.DataFrame:
        """
        Generate training data
        """
        # Features
        X = np.random.rand(self.size, 1) * 10

        # Zielvariable mit etwas Rauschen
        y = 2 * X + 1 + np.random.randn(self.size, 1) * 2

        return pd.DataFrame(
            data=np.concatenate((X, y), axis=1),
            columns=['Feature', 'Target']
        )
