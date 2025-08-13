# PIPELINE FOR STAGE 01 - DATA INGESTION


from Kidney_classifier.config.configuration import ConfigurationManager
from Kidney_classifier.components.data_ingestion import DataIngestion
from Kidney_classifier import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def data_ingestion_main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage: {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.data_ingestion_main()
        logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<<")
        print("================================================")

    except Exception as e:
        logger.exception(e)
        raise e
