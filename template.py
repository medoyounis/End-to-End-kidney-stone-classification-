import os
from pathlib import *
import logging

#create logging string:instead of print statement, use log statement
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name= 'CNNclassifier'

#creating folders
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", #code
    "templates/index.html" #for flask


]
for filepath in list_of_files:
    filepath = Path(filepath)#converts the path into windows path
    filedir, filename = os.path.split(filepath) #separate the name of the folder and the file


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")