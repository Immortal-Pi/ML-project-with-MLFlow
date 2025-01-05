import os 
import pandas as pd 
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub 
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config=config

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_squared_error(actual,pred)
        r2=r2_score(actual,pred)
        return rmse,mae,r2 
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[[self.config.target_column]]

        dagshub.init(repo_name=self.config.repo_name, repo_owner=self.config.repo_owner, mlflow=True)
        tracking_uri_type_store=urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            predicted_qualities=model.predict(test_x)
            (rmse,mae,r2)=self.eval_metrics(test_y,predicted_qualities)

            #saving metrics as local 
            scores= {'rmse': rmse,'r2_score':r2,'mae':mae}
            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)
            
            if tracking_uri_type_store!='file':
                # register the model
                mlflow.sklearn.log_model(model,'model',registered_model_name='ElasticnetModel')
            else:
                mlflow.sklearn.log_model(model,'model')

