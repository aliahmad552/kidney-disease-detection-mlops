import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s:')

project_name = "kidney"

list_of_files = [
    '.github/workflows/.gitkeep'
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/utils/__init__.py",

    "Dockerfile",
    "requirements.txt",
    "Readme.md",
    'dvc.yaml',
    'params.yaml',
    'research/trials.ipynb',
    'setup.py',
    '.dockerignore',
    '.gitignore'
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    if not os.path.exists(filedir):
        os.makedirs(filedir)
        logging.info(f"Created directory: {filedir}")
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filepath}")