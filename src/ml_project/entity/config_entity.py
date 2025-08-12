#1-- This code is for entity/config_entity.py file 
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataingestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path