import os
import gdown
import subprocess

def download_file_from_google_drive(file_url, destination):
    """
    Downloads a file from Google Drive using gdown.
    """
    gdown.download(file_url, destination, quiet=False)
    print(f"Downloaded file to {destination}")

def extract_rar_file(rar_path, extract_to):
    """
    Extracts a .rar file using the unrar utility.
    """
    os.makedirs(extract_to, exist_ok=True)
    try:
        subprocess.run(["unrar", "x", "-y", rar_path, extract_to], check=True)
        print(f"Extracted .rar file to {extract_to}")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e}")
        raise
    
if __name__ == "__main__":
    file_url = "https://drive.google.com/uc?export=download&id=1R9ULenBDBslRwdpsMbfdsiBLobcfxYIO"
    
    destination = "./model_files.rar"
    extract_to = "./models/"

    os.makedirs(extract_to, exist_ok=True)

    download_file_from_google_drive(file_url, destination)

    extract_rar_file(destination, extract_to)

    os.remove(destination)