from cryptography.fernet import Fernet
import os

# Generate a random encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Directory to store encrypted files
ENCRYPTED_FILES_DIR = "encrypted_files"

# Ensure the encrypted files directory exists
if not os.path.exists(ENCRYPTED_FILES_DIR):
    os.makedirs(ENCRYPTED_FILES_DIR)

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    
    # Extract the original filename without the path
    original_filename = os.path.basename(file_path)
    
    # Construct the encrypted file path
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, f"encrypted_{original_filename}")
    
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{original_filename}' encrypted and saved as '{os.path.basename(encrypted_file_path)}'.")

# Main function
def main():
    while True:
        file_path = input("Enter the path of the file to encrypt (or 'quit' to exit): ")

        if file_path.lower() == "quit":
            break

        if os.path.isfile(file_path):
            encrypt_file(file_path, key)
        else:
            print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()
