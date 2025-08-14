
### KIDNEY DISEASE CLASSIFICATION WITH MLFOW AND DVC

##### `Project Overview`

The purpose of this project is to develop a complete end-to-end deep learning model for kidney disease classification and track the workflow using `MLFLOW` and `DVC` for producing complete deep learning pipeline.

This project demonstrates reproducible, modular, and version-controlled deep learning pipelines leveraging on data version control dvc, available here: [DVC](https://dvc.org/doc) and track with: [MLFLOW](https://mlflow.org/docs/latest/ml/). 

The dagshub provides an open source to connect the github reposition for this project to and track the model performance with mlflow. The documentation for dagshub is available here: [DAGSHUB](https://dagshub.com/docs/index.html)

This pipeline uses DVC to manage data, models, and experiment artifacts, while Git handles code and workflow definitions and the mlflow is used for model experimentation and tracking. This ensures the workflow is collaborative, auditable, and easy to reproduce at any time, allowing for collaboration and improvement.


##### `Data Available`

The purpose of this project is just to demonstrates an end-to-end deep learning pipeline with mlflow and dvc and hence, I worked a very simple dataset of the kidney_disease_ct_scan images (Normal and Tumor).

###### `data download link`
```bash
https://drive.google.com/file/d/10qNYUcIT9QIQ9m1yndnLk8NSNu83BrCk/view?usp=sharing
```

```bash
The link to download the data from the notebook. Replace FILE_ID with the actual file_id which is the '33 hashed codes' from the link of the data from the drive.
prefix_download_url = "https://drive.google.com/uc?id=FILE_ID&export=download"

prefix_download_url = "https://drive.google.com/uc?/export=download&id=FILE_ID"

prefix_download_url = "https://drive.google.com/file/d/FILE_ID/view?usp=sharing&export=download"
```


##### `Project Execution Structures`
```bash
On this project, the deep learning `stages` include:

    - Create config.yaml
    - Create params.yaml
    - Create the entity
    - Create the configuration manager in src/config
    - Create the components
    - Create the pipeline
    - Create the main.py
    - Create the mlflow.py
    - Create the dvc.yaml
```

##### `Update Project Execution Structures`
```bash
For each step or stages, all the below need to be updated:

    - Update config.yaml
    - Update params.yaml
    - Update the entity
    - Update the configuration manager in src/config
    - Update the components
    - Update the pipeline
    - Update the main.py
    - Update the mlflow.py
    - Update the dvc.yaml
```


##### `Project Setup Instructions`

```bash

download Python 3.11.9 from python.org

Set up the Python Virtual Environment: 
     - python -m venv name_of_your_virtual_environment

     - py -3.11 -m venv name_of_the_environment

Activate the Python Virtual Environment:

     - source name_of_your_virtual_environment/bin/activate - for MacOS

    -  name_of_your_virtual_environment\Scripts\activate - for Windows

Clone the Repository: git clone https://github.com/larrysman/kidney-disease-classification-with-DVC-and-MLFlow.git

Install Project Dependencies: pip install -r requirements.txt

Configure DVC remote Storage: dvc remote add -d myremote ./dvcstore or dvc remote add -d myremote /path/to/your/dvcstore

Pull data and models tracked by DVC: dvc pull

Running and Reproducing the Pipeline: dvc repro
```


##### `Create dagshub account` 

[DAGSHUB_ACCOUNT_CREATION](https://dagshub.com/)

After creating your account, complete the profile and proceed to `create`. You will be able to connect your github repository to the `dagshub` for mlflow tracking and experimentation.


##### `Setup credentials on dagshub`

```bash
# CRREDENTIAL
"MLFLOW_TRACKING_URL"="https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow"
"MLFLOW_TRACKING_USERNAME"="USER_NAME"
"MLFLOW_TRACKING_PASSWORD"="40_HASH_TOKENS"


# ACCESS CREDENTIALS ON JUPYTER
os.environ["MLFLOW_TRACKING_URL"]="https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="USER_NAME"
os.environ["MLFLOW_TRACKING_PASSWORD"]="40_HASH_TOKENS"
```


##### `EXECUTE ON THE TERMINAL`

```bash
# EXECUTABLE AT THE TERMINAL BEFORE INITIALIZING THE MLFLOW

export MLFLOW_TRACKING_URL=https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow

export MLFLOW_TRACKING_USERNAME=USER_NAME

export MLFLOW_TRACKING_PASSWORD=40_HASH_TOKENS

Notes:
    run each on the terminal before you start the dagshub and mlflow.

    replace USER_NAME, PROJECT_NAME_OR_REPO and 40_HASH_TOKENS.
```


##### `Complete pipeline`


`run: dvc dag`

![alt text](image.png)


`run: dvc dag --outs`

![alt text](image-1.png)



##### `MLFLOW TRACKERS AND LOGGERS`





##### `Contributions and Collaboration` 👩🏻‍🤝‍👨🏽

For any contributions or collaboartion, ensure you follow the procedures below:

    You can change data or code (for instance, in src/) and to track new or updated data files do: `dvc add data/<new-data-file>`
    You will need to reproduce the pipeline to re-run all stages as needed and do: `dvc repro`
    You will need to commit code and DVC meta-files, hence do the following:

        git add .

        git commit -m "Describe your changes explicitly"

        git push

You will need to push data and models to DVC remote do: `dvc push`

Please note: Remember, contributing to open source projects is more than just a code. You can also contribute by reporting bugs, suggesting new features, improving documentation, and more. 

Thank you for considering contributing to this project!!!🙌🙌🙌

🔚

Author
Email: Larrysman2004@yahoo.com

Name: Olanrewaju Adegoke

©️O L A L Y T I C S