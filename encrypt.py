from cryptography.fernet import Fernet
from key_generate import load_key_from_file

# encrypts single file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(plaintext)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_text)
