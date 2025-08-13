# UPDATING THE CONFIGURATION MANAGER FROM THE SRC CONFIG

import os
from src.Kidney_classifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
#from src.Kidney_classifier.constants import *
from Kidney_classifier.utils.common import read_yaml_file, create_directories
from Kidney_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingModelConfig, ModelEvaluationConfig, ModelLoggingWithMLFLOWConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):


        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)

        create_directories([self.config.artifacts_root])

    # CONFIGURATION MANAGER METHOD FOR DATA INGESTION
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    

    # CONFIGURATION MANAGER METHOD FOR PREPARE_BASE_MODEL SINCE THEY HAVE THE SAME __INIT__
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE,
            params_include_top=params.INCLUDE_TOP,
            params_epochs=params.EPOCHS,
            params_classes=params.CLASSES,
            params_weights=params.WEIGHTS,
            params_learning_rate=params.LEARNING_RATE
        )

        return prepare_base_model_config
    

    # CONFIGURATION MANAGER METHOD FOR TRAINING THE MODEL SINCE THEY HAVE THE SAME __INIT__
    def get_training_model_config(self) -> TrainingModelConfig:
        config_for_training = self.config.training_model
        prepare_base_model = self.config.prepare_base_model
        params = self.params.prepare_base_model
        training_data_access = os.path.join(self.config.data_ingestion.unzip_dir)

        create_directories([Path(config_for_training.root_dir)])

        training_model_config = TrainingModelConfig(
            root_dir=Path(config_for_training.root_dir),
            trained_model_path=Path(config_for_training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data_access),
            params_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE,
            params_epochs=params.EPOCHS
        )

        return training_model_config
    

    # CONFIGURATION MANAGER METHOD FOR EVALUATING THE TRAINED MODEL SINCE THEY HAVE THE SAME __INIT__
    def get_evaluation_config(self) -> ModelEvaluationConfig:
        all_eval_config = self.config.model_evaluation
        all_eval_params = self.params.prepare_base_model

        eval_config = ModelEvaluationConfig(
            trained_model_path=Path(all_eval_config.trained_model_path),
            training_data=Path(all_eval_config.training_data),
            scores_file_path=Path(all_eval_config.scores_file_path),
            all_params = self.params.prepare_base_model,
            params_augmentation=all_eval_params.AUGMENTATION,
            params_image_size=all_eval_params.IMAGE_SIZE,
            params_batch_size=all_eval_params.BATCH_SIZE,
            params_epochs=all_eval_params.EPOCHS
        )

        return eval_config
    
    
    # CONFIGURATION MANAGER METHOD FOR LOGGING AND TRACKING MODEL EXPERIMENTATION WITH MLFLOW AND SINCE THEY HAVE THE SAME __INIT__
    def get_mlflow_config(self) -> ModelLoggingWithMLFLOWConfig:
        all_mlflow_config = self.config.model_logging_with_mlflow
        all_mlflow_params = self.params.prepare_base_model
        
        mlflow_config = ModelLoggingWithMLFLOWConfig(
            trained_model_path=Path(all_mlflow_config.trained_model_path),
            scores_file_path=Path(all_mlflow_config.scores_file_path),
            #all_params = self.params.prepare_base_model,
            all_params = all_mlflow_params,
            mlflow_url=all_mlflow_config.mlflow_url
        )

        return mlflow_config
    