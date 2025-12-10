import sys
import os
from src.kidney.utils.exceptions import CustomException
from src.kidney.utils.common import load_config, create_directories, copy_data
from src.kidney.utils.logger import logger
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    drive_path: str
    local_data_file: str

class DataIngestion:
    def __init__(self):
        try:
            cfg = load_config()
            self.config = DataIngestionConfig(
                root_dir = cfg['data_ingestion']['root_dir'],
                drive_path = cfg['data_ingestion']['drive_path'],
                local_data_file = cfg['data_ingestion']['local_data_file']

            )

            logger.info(f"DataIngestionConfig: {self.config}")
        except Exception as e:
            raise CustomException(f"Data Ingestion Failed {e}", sys)
        
        print("Checking Drive Path Exists:", os.path.exists(self.config.drive_path))
        print("Path:", self.config.drive_path)
    def ingest_data(self):
        try:
            logger.info("📥 Starting Data Ingestion...")

            # Create artifact directory
            create_directories([self.config.root_dir])

            target_path = os.path.join(self.config.root_dir, self.config.local_data_file)

            logger.info(f"Copying data from: {self.config.drive_path}")
            logger.info(f"Saving data to: {target_path}")

            copy_data(self.config.drive_path, target_path)

            logger.info("✅ Data Ingestion Completed Successfully")

            return target_path

        except Exception as e:
            raise CustomException(f"Data Ingestion Failed: {e}", sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    obj.ingest_data()
        
