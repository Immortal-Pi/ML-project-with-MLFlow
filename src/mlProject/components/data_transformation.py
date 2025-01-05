import os 
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd 
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 

    ### Note: add different data transformation techinques such as Scalar, PCA and all
    # You can perform all kind of EDA in ML cycle here before passing this data to the model 

    def train_test_spliting(self):

        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info('Splited data into training and test set')
        logger.info(f'training set shape : {train.shape}')
        logger.info(f'testing set shape : {test.shape}')