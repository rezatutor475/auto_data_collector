import logging
from datetime import datetime
import uuid
import os
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def log_info(message: str):
    logging.info(message)

def log_warning(message: str):
    logging.warning(message)

def log_error(message: str):
    logging.error(message)

def current_timestamp() -> str:
    """
    Returns current timestamp as string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def safe_cast(val, to_type, default=None):
    """
    Tries to cast a value to a given type. Returns default if it fails.
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def generate_uuid() -> str:
    """
    Generates a new UUID4 string.
    """
    return str(uuid.uuid4())

def ensure_directory(path: str):
    """
    Ensures that the directory exists.
    """
    os.makedirs(path, exist_ok=True)

def read_json_file(file_path: str):
    """
    Reads and parses a JSON file.
    """
    if not os.path.exists(file_path):
        log_warning(f"File not found: {file_path}")
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(data, file_path: str):
    """
    Writes data to a JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        log_info(f"Data written to {file_path}")
