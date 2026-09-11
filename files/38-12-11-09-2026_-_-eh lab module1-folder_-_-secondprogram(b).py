from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Load original file data
with open("confidential.txt", "rb") as file:
    file_data = file.read()

# Load signature
with open("confidential.signature", "rb") as sig_file:
    signature = sig_file.read()

# Verify the signature
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
    print("✅ Signature is valid.")

except Exception as e:
    print("❌ Signature is NOT valid:", str(e))
