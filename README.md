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


## AWS CICD Deployment with Github Actions 

### 1. Login to AWS console

### 2. Create IAM user for deployment 

``` bash 
# with access 
1. ECR access : It is vurtual machine 
2. ECR: Elastic Container registry to save your docker image in AWS

# Description: About the deployment 
1. Build docker image of the source code 
2. Push your docker image to ECR
3. Launch Your EC2
4. Pull your image from ECR in EC2
5. Launch your docker image in EC2

# Policy 
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
```
### 3. Create ECR repo to store/save docker image 
``` bash
- Save the URI: 011528265658.dkr.ecr.us-east-2.amazonaws.com/mlproj
```
### 4. Create EC2 machine (Ubuntu)
### 5. Open EC2 and install docker in EC2 Machine:
```bash
# optional 
sudo apt-get update -y
sudo apt-get upgrade -y 

# required 
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu 
newgrp docker 
```
### 6. Configure EC2 as self-hosted runner: 
``` bash 
settings> actions> runner>new self hosted runner > choose os > then sun the command one by one 
```
### 7. setup github secrets 
``` bash
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = us-east-1
AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com
ECR_REPOSITORY_NAME = simple-app
```




