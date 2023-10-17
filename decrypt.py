from cryptography.fernet import Fernet
from key_generate import load_key_from_file

# decrpyts single file
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_text = file.read()
    
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    
    with open(encrypted_file_path, 'wb') as file:
        file.write(decrypted_text)
