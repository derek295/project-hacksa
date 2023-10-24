from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Load the private key
with open("private_key.pem", "rb") as private_key_file:
    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=None,
        backend=default_backend()
    )

# Directory for storing decrypted files
DECRYPTED_FILES_DIR = "decrypted_files"
if not os.path.exists(DECRYPTED_FILES_DIR):
    os.makedirs(DECRYPTED_FILES_DIR)

# Function to decrypt a file
def decrypt_file(file_path, private_key):
    with open(file_path, "rb") as encrypted_file:
        data = encrypted_file.read()
    decrypted_data = private_key.decrypt(data, padding.PKCS1v15())
    
    # Construct the path for the decrypted file
    decrypted_file_path = os.path.join(DECRYPTED_FILES_DIR, f"decrypted_{os.path.basename(file_path)}")
    
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"File decrypted and saved as '{os.path.basename(decrypted_file_path)}'.")

# Main function
if __name__ == "__main__":
    file_path = input("Enter the path of the file to decrypt: ")
    if os.path.exists(file_path):
        decrypt_file(file_path, private_key)
    else:
        print("File not found. Please enter a valid file path.")
