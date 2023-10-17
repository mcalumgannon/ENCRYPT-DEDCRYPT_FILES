from cryptography.fernet import Fernet

key = Fernet.generate_key()
filename = 'key.key'
# saves the random key to a file called key.key
def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)


# opening the file
def load_key_from_file(filename):
    with open(filename, 'rb') as key_file:
        key = key_file.read()
    return key