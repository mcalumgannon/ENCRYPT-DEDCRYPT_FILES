from key_generate import save_key_to_file
from cryptography.fernet import Fernet

# make key
key = Fernet.generate_key()
filename = 'key.key'

save_key_to_file(key, filename)