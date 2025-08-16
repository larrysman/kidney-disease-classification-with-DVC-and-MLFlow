# MODEL EXPERIMENTATION TRACKING AND LOGGING WITH MLFLOW

import tensorflow as tf
import mlflow
import mlflow.keras
import json
from urllib.parse import urlparse
from Kidney_classifier import logger
from src.Kidney_classifier.entity.config_entity import ModelLoggingWithMLFLOWConfig


class MLFLOWLogger:
    def __init__(self, config: ModelLoggingWithMLFLOWConfig):
        self.config = config

    def load_evaluation_scores(self):
        with open(self.config.scores_file_path, "r") as file:
            return json.load(file)
        

    def load_trained_model(self):
        return tf.keras.models.load_model(self.config.trained_model_path)
    
    def run_mlflow_log(self):
        scores = self.load_evaluation_scores()
        model = self.load_trained_model()

        mlflow.set_tracking_uri(self.config.mlflow_url)
        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)


            if tracking_url_type_store != "file":
                mlflow.keras.log_model(
                    model, artifact_path="model", registered_model_name="KIDNEY_DISEASE_CLASSIFIER_FROM_VGG16Model", keras_model_kwargs={"save_format": "h5"}
                )

            else:
                mlflow.keras.log_model(model, "model", keras_model_kwargs={"save_format": "h5"})