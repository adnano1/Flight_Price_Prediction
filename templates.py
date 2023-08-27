import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

list_of_file = [

    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",
    "requirements.txt",
    "app.py",
    "READEME.md",
    "setup.py",
    "Dockerfile"
]

for filepath in list_of_file:
    
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    logging.info(f'Created Folders for {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'wb'):
            pass

        logging.info(f'File Created {filename}')

    else:
        logging.info('File already exists')