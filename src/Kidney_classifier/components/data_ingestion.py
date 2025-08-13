# UPDATE THE COMPONENTS FOR DATA INGESTION

import os
import zipfile
import gdown
from Kidney_classifier import logger
from Kidney_classifier.utils.common import get_size
from Kidney_classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self) -> str:
        """
        Fetching data from the google drive
        """

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} into the file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            full_download_url = prefix + file_id
            gdown.download(full_download_url, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into the file {zip_download_dir}")

        except Exception as e:
            raise e

    
    def extract_zip_file(self):
        """
        Args:
            zip_file_path: str
            Extracts the zip file into the data directory.

        Returns:
            None

        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)


    