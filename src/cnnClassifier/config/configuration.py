from src.cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbacksConfig)
from cnnClassifier import logger

class ConfigurationManager:
    def __init__(self,config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_URL = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        return data_ingestion_config
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        prepare_base_model_config = PrepareBaseModelConfig(
                    root_dir = Path(config.root_dir),
                    base_model_path = Path(config.base_model_path),
                    updated_base_model_path = Path(config.updated_base_model_path),
                    params_image_size = self.params.IMAGE_SIZE,
                    params_learning_rate = self.params.LEARNING_RATE,
                    params_classes = self.params.CLASSES,
                    params_epochs = self.params.EPOCHS,
                    params_include_top = self.params.INCLUDE_TOP,
                    params_weights = self.params.WEIGHTS
                )
        return prepare_base_model_config

    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(model_ckpt_dir), Path(config.tensorboard_root_log_dir)])
        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config