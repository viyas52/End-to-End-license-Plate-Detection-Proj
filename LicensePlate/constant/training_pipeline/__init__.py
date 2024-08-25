import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1UMLPZyR6LDlJ2MmpUhtlDwEYZSCWJpfi/view?usp=drive_link"

DATA_FILE_NAME:str = "LicensePlate_Data.zip"



"""
Data Validation 
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["test", "train", "data.yaml"]



"""
MODEL TRAINER 
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov10n.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 1
