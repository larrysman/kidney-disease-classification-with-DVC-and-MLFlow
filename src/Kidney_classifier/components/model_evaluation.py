# MODEL EVALUATION MODULE

import tensorflow as tf
from pathlib import Path
from Kidney_classifier import logger
from src.Kidney_classifier.entity.config_entity import ModelEvaluationConfig
from Kidney_classifier.utils.common import save_json_file


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.model = None
        self.score = None
        self.validation_generator = None

    def _testing_validation_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.10
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.validation_generator = validation_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_trained_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def model_evaluate(self):
        """
        This methods loads the trained model,
        evaluate its performance on validation set, and save the results.
        """
        self.model = self.load_trained_model(self.config.trained_model_path)
        self._testing_validation_generator()
        self.score = self.model.evaluate(self.validation_generator)
        self.save_score()
        return self.model, self.score

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        self.config.scores_file_path.parent.mkdir(parents=True, exist_ok=True)
        save_json_file(path=self.config.scores_file_path, data=scores)