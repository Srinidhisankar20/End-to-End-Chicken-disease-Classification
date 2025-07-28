import os
from box.exceptions import BoxValueError
import yaml
from pathlib import Path
import joblib
from typing import Union
import json
from ensure import ensure_annotations
from typing import Any
import base64
from cnnClassifier import logger
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml: Union[Path,str]) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a dictionary.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        dict: Content of the YAML file.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or not found.")
    except Exception as e:
        raise e 
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (str): Path to the JSON file.
        data (dict): Data to save.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Data saved to {path} successfully.")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its content as a ConfigBox.
    
    Args:
        path (str): Path to the JSON file.
        
    Returns:
        ConfigBox: Content of the JSON file.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file {path} loaded successfully.")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.
    
    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Data saved to {path} successfully.")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Loaded data.
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from {path} successfully.")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in a human-readable format.
    
    Args:
        path (Path): Path to the file.
        
    Returns:
        str: Size of the file in a human-readable format.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

@ensure_annotations
def encodeimageintobase64(croppedImagePath):
   with open(croppedImagePath, "rb") as imageFile:
       encoded_string = base64.b64encode(imageFile.read())
       return encoded_string
   
@ensure_annotations
def decodebase64toimage(encoded_string, output_path):
    """
    Decodes a base64 encoded string and saves it as an image file.
    
    Args:
        encoded_string (str): Base64 encoded string.
        output_path (str): Path to save the decoded image.
    """
    image_data = base64.b64decode(encoded_string)
    with open(output_path, 'wb') as image_file:
        image_file.write(image_data)    
        image_data.close()