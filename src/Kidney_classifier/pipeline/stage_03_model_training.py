# PIPELINE FOR STAGE 03 - MODEL TRAINING


from Kidney_classifier.config.configuration import ConfigurationManager
from Kidney_classifier.components.model_training import ModelTraining
from Kidney_classifier import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def model_training_main(self):
        config = ConfigurationManager()
        training_model_config = config.get_training_model_config()
        training_model = ModelTraining(config=training_model_config)
        training_model.get_updated_base_model()
        training_model.training_validation_generator()
        training_model.model_training()



if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.model_training_main()
        logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
        print("=================================================")

    except Exception as e:
        logger.exception(e)
        raise e