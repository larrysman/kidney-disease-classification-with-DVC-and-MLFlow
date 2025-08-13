# UPDATE THE MAIN 

from src.Kidney_classifier import logger
from src.Kidney_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Kidney_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Kidney_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.Kidney_classifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from src.Kidney_classifier.pipeline.stage_05_mlflow_experimentation import MLFLOWExperimentationPipeline


# STAGE 01
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.data_ingestion_main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
    print("=================================================")

except Exception as e:
    logger.exception(e)
    raise e



# STAGE 02
STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"****************************************")
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.prepare_base_model_main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
    print("=================================================")

except Exception as e:
    logger.exception(e)
    raise e



# STAGE 03
STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.model_training_main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
    print("=================================================")

except Exception as e:
    logger.exception(e)
    raise e



# STAGE 04
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.model_evaluation_main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
    print("=================================================")

except Exception as e:
    logger.exception(e)
    raise e


# STAGE 05
STAGE_NAME = "MLFLOW Experimentation Stage"

try:
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
    obj = MLFLOWExperimentationPipeline()
    obj.mlflow_experimentation_main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
    print("=================================================")

except Exception as e:
    logger.exception(e)
    raise e