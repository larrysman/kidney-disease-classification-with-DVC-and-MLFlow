# PROJECT FILES AND FOLDERS STRUCTURE FOR KIDNEY DISEASE CLASSIFICATION PROJECT

import os
import logging
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "Kidney_classifier"


# CREATE THE PROJECT DIRECTORY AND FILES

list_of_files_and_folders = [
    f".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"requirements.txt",
    f"setup.py",
    f"config/config.yaml",
    f"dvc.yaml",
    f"params.yaml",
    f"research/trial.ipynb",
    f"templates/index.html",
    f"README.md"
]


# FUNCTION TO CREATE THE PROJECT STRUCTURE

def create_project_structure(list_of_files_and_folders: List[str]) -> None:
    """
    Create the project structure based on the provided list of files and folders.
    If a file or folder does not exist, it will be created.
    If a file exists but is empty, it will be created as an empty file.

    Args:
        List: List containing the files and folders.

    Returns:
        None
    """
    for file_path in list_of_files_and_folders:
        file_path = Path(file_path)
        filedir, filename = os.path.split(file_path)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                pass
            logging.info(f"Creating empty file: {file_path}")

        else:
            logging.info(f"File already exists: {file_path} and is not empty.")


if __name__ == "__main__":
    create_project_structure(list_of_files_and_folders)
    logging.info(f"Project structure for '{project_name}' created successfully.")
