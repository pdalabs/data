from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_message = pad(message.encode("utf-8"), AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return cipher.iv, ciphertext


def decrypt_aes(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_padded_message = cipher.decrypt(ciphertext)
    plaintext = unpad(
        decrypted_padded_message,
        AES.block_size
    ).decode("utf-8")
    return plaintext


# AES key: 16, 24, or 32 bytes
key_aes = get_random_bytes(32)

message = "This is a secret message for AES!"

iv_aes, encrypted_message_aes = encrypt_aes(message, key_aes)

decrypted_message_aes = decrypt_aes(
    iv_aes,
    encrypted_message_aes,
    key_aes
)

print("AES Encrypted:", encrypted_message_aes)
print("AES Decrypted:", decrypted_message_aes)
