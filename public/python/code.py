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
    # Save the uploaded file to a temporary location
    original_filename = os.path.basename(uploaded_file.filename)
    file_path = os.path.join(ENCRYPTED_FILES_DIR, f"encrypted_{original_filename}")
    
    with open(file_path, 'wb') as encrypted_file:
        while True:
            chunk = uploaded_file.file.read(8192)
            if not chunk:
                break
            encrypted_chunk = fernet.encrypt(chunk)
            encrypted_file.write(encrypted_chunk)
    
    print(f"File '{original_filename}' uploaded and encrypted successfully as '{os.path.basename(file_path)}'.")
else:
    print("File not found. Please select a file for upload.")
