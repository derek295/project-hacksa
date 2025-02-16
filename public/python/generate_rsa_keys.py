from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
   public_exponent=65537,
   key_size=2048,
   backend=default_backend()
)

private_pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.NoEncryption()
)

with open("private_key.pem", "wb") as private_key_file:
   private_key_file.write(private_pem)

public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("public_key.pem", "wb") as public_key_file:
   public_key_file.write(public_pem)
