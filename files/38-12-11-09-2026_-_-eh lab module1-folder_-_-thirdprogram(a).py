from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_des3(message, key):
    cipher = DES3.new(key, DES3.MODE_CBC)
    padded_message = pad(message.encode('utf-8'), DES3.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return cipher.iv, ciphertext

def decrypt_des3(iv, ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    decrypted_padded_message = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_message, DES3.block_size).decode('utf-8')
    return plaintext

# Example Usage
key_des3 = get_random_bytes(24)  # 24 bytes for Triple DES
message = "This is a secret message for DES!"

iv_des3, encrypted_message_des3 = encrypt_des3(message, key_des3)
decrypted_message_des3 = decrypt_des3(iv_des3, encrypted_message_des3, key_des3)
print("DES3 Encrypted:", encrypted_message_des3)

print("DES3 Decrypted:", decrypted_message_des3)
