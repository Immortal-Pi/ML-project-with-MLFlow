import os 
from mlProject import logger
from mlProject.config.configuration import DataValidationConfig
import pandas as pd 
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_all_columns(self)->bool:
        try:
            validate_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=data.dtypes.to_dict()
            all_schema=self.config.all_schema
            
            for (key1,value1), (key2,value2) in zip(all_cols.items(), all_schema.items()):
                if key1 != key2 or value1 !=value2:         
                    validate_status=False 
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation status: {validate_status}')
                else:
                    validate_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation status: {validate_status}')
            return validate_status
        except Exception as e:
            raise e 