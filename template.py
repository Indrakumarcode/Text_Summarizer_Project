import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

# Define project name and list of files
project_name = "textSummarizer"
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Iterate through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Split file path into directory and filename

    if filedir != "":  # Check if the directory part is not empty
        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

        # Check if the file exists or is empty
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass  # Create an empty file
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File {filepath} already exists")
