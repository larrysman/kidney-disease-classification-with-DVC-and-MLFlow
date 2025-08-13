# UPDATING THE ENTITY FOLDER FOR THE ENTIRE WORKFLOW

from dataclasses import dataclass
from pathlib import Path


# ENTITY FOR DATA INGESTION
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


# ENTITY FOR PREPARE BASE MODEL
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_augmentation: bool
    params_image_size: list
    params_batch_size: int
    params_include_top: bool
    params_epochs: int
    params_classes: int
    params_weights: str
    params_learning_rate: float


# ENTITY FOR TRAINING THE MODEL
@dataclass(frozen=True)
class TrainingModelConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_augmentation: bool
    params_image_size: list
    params_batch_size: int
    params_epochs: int


# ENTITY FOR MODEL EVALUATION
@dataclass(frozen=True)
class ModelEvaluationConfig:
    trained_model_path: Path
    training_data: Path
    scores_file_path: Path
    all_params: dict
    params_augmentation: bool
    params_image_size: list
    params_batch_size: int
    params_epochs: int


# ENTITY FOR MLFLOW EXPERIMENTATION
@dataclass(frozen=True)
class ModelLoggingWithMLFLOWConfig:
    trained_model_path: Path
    all_params: dict
    mlflow_url: str
    scores_file_path: Path