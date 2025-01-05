# ML project with MLFlow

# DagsHub 

Clone the repository

```bash 
https://github.com/Immortal-Pi/ML-project-with-MLFlow
```
## STEP 01- create a conda environment after opening the repository

```bash
conda create -n mlopsML python=3.9 -y 
```
```bash
conda activate mlopsML
```
## STEP 02 - install the requirements
```bash 
pip install -r requirements.txt 
```

Now,
```bash
python app.py
```

## MLFlow 

#### cmd 
-mlflow ui

## dagsHub 

import dagshub
dagshub.init(repo_owner='dagshub_username', repo_name='repository_name', mlflow=True)




