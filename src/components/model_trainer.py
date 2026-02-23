import os
import sys
from dataclasses import dataclass

import numpy as np

from src.exception import CustomException
from src.logger import logging


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array: np.ndarray, test_array: np.ndarray):
        """A dummy training routine that simply logs shapes and returns a message.

        Real code would fit a model and persist it to disk.
        """
        try:
            logging.info("Starting model trainer")
            logging.info("Train array shape: %s", getattr(train_array, 'shape', None))
            logging.info("Test array shape: %s", getattr(test_array, 'shape', None))

            # No actual model – just pretend we trained something
            result = {
                "train_shape": train_array.shape if hasattr(train_array, 'shape') else None,
                "test_shape": test_array.shape if hasattr(test_array, 'shape') else None,
                "model_path": self.config.trained_model_file_path,
            }

            logging.info("Model training completed (dummy)")
            return result
        except Exception as e:
            raise CustomException(e, sys)
