import os
import gdown
from unrar import rarfile

def download_file_from_google_drive(file_url, destination):
    """
    Downloads a file from Google Drive using gdown.
    """
    gdown.download(file_url, destination, quiet=False)
    print(f"Downloaded file to {destination}")

def extract_rar_file(rar_path, extract_to):
    """
    Extracts a .rar file to the specified directory using the unrar library.
    """
    with rarfile.RarFile(rar_path) as rf:
        rf.extractall(extract_to)
    print(f"Extracted .rar file to {extract_to}")

if __name__ == "__main__":
    file_url = "https://drive.google.com/uc?export=download&id=1R9ULenBDBslRwdpsMbfdsiBLobcfxYIO"
    
    destination = "./model_files.rar"
    extract_to = "./models/"

    os.makedirs(extract_to, exist_ok=True)

    download_file_from_google_drive(file_url, destination)
    extract_rar_file(destination, extract_to)

    os.remove(destination)
