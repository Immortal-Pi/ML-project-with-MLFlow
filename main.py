from mlProject import logger
from mlProject.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline


STAGE_NAME='Data Ingestion stage'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 