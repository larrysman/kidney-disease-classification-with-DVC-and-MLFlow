# PIPELINE FOR STAGE 04 - MODEL EVALUATION

from Kidney_classifier.config.configuration import ConfigurationManager
from Kidney_classifier.components.model_evaluation import ModelEvaluation
from Kidney_classifier import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def model_evaluation_main(self):
        
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.model_evaluate()



if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.model_evaluation_main()
        logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
        print("=================================================")

    except Exception as e:
        logger.exception(e)
        raise e