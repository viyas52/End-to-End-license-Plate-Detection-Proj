import os,sys
import yaml
import shutil

from LicensePlate.utils.main_utils import read_yaml_file

from LicensePlate.logger import logging
from LicensePlate.exception import CustomException

from LicensePlate.entity.config_entity import ModelTrainerConfig
from LicensePlate.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            # Unzipping data
            logging.info("Unzipping data")
            os.system("tar -xvf LicensePlate_Data.zip")  # Use tar for unzipping; replace if you have a different tool
            os.remove("LicensePlate_Data.zip")
            logging.info("Unzip successful")
            
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            command = f'yolo task=detect mode=train model={model_config_file_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 batch={self.model_trainer_config.batch_size}'
            # Training the model
            os.system(command)

            # Copying the trained model weights
            source_path = "runs\\detect\\train\\weights\\best.pt"
            destination_path = self.model_trainer_config.model_trainer_dir
            os.makedirs(destination_path, exist_ok=True)
            shutil.copy(source_path, destination_path)

            # Removing directories and files
            os.system("rmdir /s /q runs")
            os.system("rmdir /s /q train")
            os.system("rmdir /s /q test")
            os.system("del data.yaml")
            os.system("del yolov10n.pt")

            # Creating and returning the model trainer artifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=os.path.join(destination_path,"best.pt")
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise CustomException(e, sys)