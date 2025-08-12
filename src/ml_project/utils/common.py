import os
from box.exceptions import BoxValueError
import yaml
from ml_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# 1st function ---> READ YAML FILE

@ensure_annotations
def read_yaml(path_location:Path) -> ConfigBox:
    with open(path_location) as file:
        content = yaml.safe_load(file)
        return ConfigBox(content)
    

# 2nd function ----> CREATE DIRECTORY
@ensure_annotations
def create_dir(dir_file_loc:list,verbose =True):
    for path in dir_file_loc:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("Directory created successfully")

# 3rd function -----> SAVE JSON
@ensure_annotations
def save_json(path:Path,data:dict):   #mtln ki path dedo jaha pr save krwana hai json format ko aur data dedo jo ki dict format mai hoga
    with open (path, 'w') as f:
        json.dump(data,f,indent=4)

#4th function ----> LOAD JSON
@ensure_annotations
def load_json(path:Path) ->ConfigBox:
    with open(path) as f:
        content = json.load(f)
        return ConfigBox(content)
    

#5th function ----->LOAD BIN
@ensure_annotations
def load_bin(path:Path) ->object:
    data = joblib.load(path)
    return data

#6th function -----> SAVE BIN
@ensure_annotations
def save_bin(path:Path,data:object):
    joblib.dump(value=data,filename=path)


#7th function ----> GET SIZE
@ensure_annotations
def getsize(path:Path) ->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"








