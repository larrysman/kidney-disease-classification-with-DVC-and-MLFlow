# PIPELINE FOR STAGE 05 - MLFLOW MODEL EXPERIMENTATION, TRACKING AND LOGGING

from Kidney_classifier.config.configuration import ConfigurationManager
from Kidney_classifier.components.model_tracking_with_mlflow import MLFLOWLogger
from Kidney_classifier import logger



STAGE_NAME = "MLFLOW Experimentation Stage"

class MLFLOWExperimentationPipeline:
    def __init__(self):
        pass

    def mlflow_experimentation_main(self):
        
        config = ConfigurationManager()
        mlflow_logger_config = config.get_mlflow_config()
        mlflow_logger = MLFLOWLogger(config=mlflow_logger_config)
        mlflow_logger.run_mlflow_log()



if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
        obj = MLFLOWExperimentationPipeline()
        obj.mlflow_experimentation_main()
        logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
        print("=================================================")

    except Exception as e:
        logger.exception(e)
        raise e