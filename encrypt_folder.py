from cryptography.fernet import Fernet
from encrypt import encrypt_file
from decrypt import decrypt_file
from key_generate import load_key_from_file
import os

folder_path = 'E_and_D_crypt_folder'

# encrypts folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        encrypt_file(file_path, load_key_from_file('key.key'))


