import os
import shutil

UPLOAD_DIR = 'uploads'

def upload(csv_file):

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)  

    shutil.copy(csv_file, UPLOAD_DIR)
    
    print(f'Uploaded {csv_file} to {UPLOAD_DIR}')