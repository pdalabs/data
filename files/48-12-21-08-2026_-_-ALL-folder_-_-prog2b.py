from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
with open("public_key.pem","rb") as f:
    public_key=serialization.load_pem_public_key(f.read())
with open("confidential.txt","rb") as file:
    file_data=file.read()
with open("confidential.signature","rb") as sig_file:
    signature=sig_file.read()
try:
    public_key.verify(
        signature,
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
            ),
        hashes.SHA256()
        )
    print("signature is valid")
except Exception as e:
    print("signature is Not Valid:",str(e))



