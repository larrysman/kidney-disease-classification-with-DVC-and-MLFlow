# KIDNEY DISEASE CLASSIFICATION WITH MLFOW AND DVC


# SETTING UP THE PROJECT

### WORKFLOWS
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

#### DATA LINK
```bash
https://drive.google.com/file/d/10qNYUcIT9QIQ9m1yndnLk8NSNu83BrCk/view?usp=sharing
```

```bash
The link to download the data from the notebook. Replace FILE_ID with the actual file_id which is the '33 hashed codes' from the link of the data from the drive.
prefix_download_url = "https://drive.google.com/uc?id=FILE_ID&export=download"

prefix_download_url = "https://drive.google.com/uc?/export=download&id=FILE_ID"

prefix_download_url = "https://drive.google.com/file/d/FILE_ID/view?usp=sharing&export=download"
```

### STEPS:
Clone the repository

```bash
https://github.com/larrysman/kidney-disease-classification-mlflow-and-dvc
```

### STEP 01 - INSTALL PYTHON AND CREATE PYTHON ENVIRONMENT FOR THE PROJECT

```bash
download Python 3.11.9 from python.org
```

```bash
py -3.11 -m venv 'name_of_the_environment'
```

```bash
name_of_the_environment/Scripts/activate
```


### STEP 02 - INSTALL THE REQUIREMENTS.TXT

```bash
pip install -r requirements.txt
```

#### MLFLOW AND DAGSHUB

###### MLFLOW

[MLFLOW](https://mlflow.org/docs/latest/ml/)


##### DAGSHUB

[DAGSHUB](https://dagshub.com/)


```bash
#### DAGSHUB IMPORT
import dagshub
dagshub.init(repo_owner='USER_NAME', repo_name='PROVIDE_REPO_NAME', mlflow=True)


#### CREDENTIALS
"MLFLOW_TRACKING_URL"="https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow"
"MLFLOW_TRACKING_USERNAME"="USER_NAME"
"MLFLOW_TRACKING_PASSWORD"="40_HASH_TOKENS"
python script.py

#### SCRIPTS
import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```

```bash
# RUNNING ON JUPYTER NOTEBOOK
os.environ["MLFLOW_TRACKING_URL"]="https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="USER_NAME"
os.environ["MLFLOW_TRACKING_PASSWORD"]="40_HASH_TOKENS"


#### EXECUTABLE AT THE TERMINAL BEFORE INITIALIZING THE MLFLOW
export MLFLOW_TRACKING_URL=https://dagshub.com/USER_NAME/PROJECT_NAME_OR_REPO.mlflow

export MLFLOW_TRACKING_USERNAME=USER_NAME

export MLFLOW_TRACKING_PASSWORD=40_HASH_TOKENS

run each on the terminal before you start the dagshub and mlflow
```





