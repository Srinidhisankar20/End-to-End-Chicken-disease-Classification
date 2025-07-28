from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.DataIngestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        obj = ConfigurationManager()
        data_ingestion_config = obj.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in stage {STAGE_NAME}: {e}")
        raise e
    