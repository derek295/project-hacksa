from cryptography.fernet import Fernet
import os
import cgi

# Generate a random encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Directory to store encrypted files
ENCRYPTED_FILES_DIR = "encrypted_files"

# Ensure the encrypted files directory exists
if not os.path.exists(ENCRYPTED_FILES_DIR):
    os.makedirs(ENCRYPTED_FILES_DIR)

# Get the uploaded file
form = cgi.FieldStorage()
uploaded_file = form['file']

if uploaded_file:
    # Extract the original filename
    original_filename = os.path.basename(uploaded_file.filename)
    
    # Construct the path for the encrypted file
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, f"encrypted_{original_filename}")
    
    # Check if a file with the same name already exists
    if os.path.exists(encrypted_file_path):
        choice = input(f"A file with the name '{original_filename}' already exists. Do you want to overwrite it? (yes/no): ")
        if choice.lower() != 'yes':
            print(f"File '{original_filename}' was not uploaded or overwritten.")
        else:
            # Overwrite the existing file
            with open(encrypted_file_path, 'wb') as encrypted_file:
                while True:
                    chunk = uploaded_file.file.read(8192)
                    if not chunk:
                        break
                    encrypted_chunk = fernet.encrypt(chunk)
                    encrypted_file.write(encrypted_chunk)
            print(f"File '{original_filename}' uploaded and encrypted successfully as '{os.path.basename(encrypted_file_path)}'.")
    else:
        # Save the uploaded file
        with open(encrypted_file_path, 'wb') as encrypted_file:
            while True:
                chunk = uploaded_file.file.read(8192)
                if not chunk:
                    break
                encrypted_chunk = fernet.encrypt(chunk)
                encrypted_file.write(encrypted_chunk)
        print(f"File '{original_filename}' uploaded and encrypted successfully as '{os.path.basename(encrypted_file_path)}'.")
else:
    print("File not found. Please select a file for upload.")
