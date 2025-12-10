import os
import shutil
import zipfile
import yaml
from src.kidney.utils.logger import logger

def create_directories(paths: list):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory: {path}")

def copy_data(src, dst):
    """
    Copies the dataset from src to dst.
    If src is a ZIP file, extract it into dst folder.
    """
    if src.endswith(".zip"):
        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall(dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)


def load_config(config_path = 'src/kidney/config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config
    logger.info(f"Loaded configuration from {config_path}")