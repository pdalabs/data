from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
def encrypt_des3(message,key):
    cipher=DES3.new(key,DES3.MODE_CBC)
    padded_message=pad(message.encode('utf-8'),DES3.blocksize)
    ciphertext=cipher_encrypt (padded_message)
    return cipher.iv,ciphertext
def decrypt_des3(iv,ciphertext,key):
    cipher=DES3.new(key,DES3.MODE_CBC,iv=iv)
    decrypted_padded_message=cipher.decrypt(ciphertext)
    plaintext=unpad(decrypted_padded_message,DES3_block_size).decode('utf-8')
    return plaintext
key_des3=get_random_bytes(24)
message="this is a secret command for des!!"
iv_des3,encrypted_message_des3=encrypt_des3(message,key_des3)
decrypted_message_des3=decrypt_des3(iv_des,encrypted_message_des3,key_des3)
print("DES3 Encrypted:",encrypted_message_des3)
print("DES3 decrypted:",decrypted_message_des3)
