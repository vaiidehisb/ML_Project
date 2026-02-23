import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    # path where any preprocessing objects would be saved
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def initiate_data_transformation(self, train_path: str, test_path: str):
        """Read the train/test csv files and return numpy arrays.

        This implementation is intentionally minimal so that the rest of the
        pipeline can run.  It does **not** perform any real preprocessing.
        """
        logging.info("Starting data transformation")
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and test dataframes loaded")

            # simply convert to numpy arrays; the caller can decide how to use them
            train_arr = train_df.values
            test_arr = test_df.values

            return train_arr, test_arr, self.config.preprocessor_obj_file_path
        except Exception as e:
            raise CustomException(e, sys)
