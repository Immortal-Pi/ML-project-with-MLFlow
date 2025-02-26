from mlProject import logger
from mlProject.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline
from mlProject.pipeline.data_validation_stage import DataValidationTrainingPipeline
from mlProject.pipeline.data_transformation_stage import DataTransformationTrainingPipeline
from mlProject.pipeline.model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.model_evalution import ModelEvaluationTrainingPipeline

STAGE_NAME='DATA INGESTION STAGE'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME='DATA VALIDATION STAGE'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='DATA TRANSFORMATION STAGE'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='MODEL TRAINER STAGE'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\n x==========x')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='MODEL EVALUTION STAGE'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x')
except Exception as e:
    logger.exception(e)
    raise e 