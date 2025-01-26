import os
import gdown
import zipfile
from configs.app_config import AppConfig

config = AppConfig.get_config_instance()

def download_file_from_google_drive(file_url, destination):
    """
    Downloads a file from Google Drive using gdown.
    """
    gdown.download(file_url, destination, quiet=False)
    print(f"Downloaded file to {destination}")

def extract_zip_file(zip_path, extract_to):
    """
    Extracts a .zip file using Python's zipfile module.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted .zip file to {extract_to}")

if __name__ == "__main__":
    file_url = "https://drive.google.com/uc?export=download&id=1MZFEaZAdICsT0k4CAX4ViqDq71hTXJZq"
    destination = str(config.MODEL_PATH / "model_files.zip")
    extract_to = str(config.MODEL_PATH)

    os.makedirs(extract_to, exist_ok=True)

    download_file_from_google_drive(file_url, destination)

    extract_zip_file(destination, extract_to)

    os.remove(destination)

