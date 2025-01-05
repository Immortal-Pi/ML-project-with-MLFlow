from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME='MODEL EVALUTION STAGE'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evalution_config=config.get_model_evaluation_config()
        model_evalution=ModelEvaluation(config=model_evalution_config)
        model_evalution.log_into_mlflow()


if __name__=='__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
        obj=ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x')
    except Exception as e:
        logger.exception(e)
        raise e 