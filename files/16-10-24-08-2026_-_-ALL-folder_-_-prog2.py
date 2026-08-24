from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent= 65537,
    key_size = 2048
)

public_key = private_key.public_key()

with open ('private_key.pem', 'wb') as f:
    f.write (private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
        ))
with open('public_key.pem','wb') as f:
    f.write(public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
with open ('confidential.txt','rb') as file:
    file_data = file.read()



signature = private_key.sign(
    file_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256()
)

with open('Confidential.signature', 'wb') as sig_file:
             sig_file.write(signature)

print("Digital signature generated and saved as confidential signature")


