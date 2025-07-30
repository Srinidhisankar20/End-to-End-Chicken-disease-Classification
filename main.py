from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_Data_Ingestion import DataIngestionPipeline  
from cnnClassifier.pipeline.stage_02_preparebasemodel import PrepareBaseModelTrainingPipeline  
from cnnClassifier.config.configuration import ConfigurationManager   

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(f"Exception occurred in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline(config=ConfigurationManager())
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(f"Exception occurred in stage {STAGE_NAME}: {e}")
    raise e
