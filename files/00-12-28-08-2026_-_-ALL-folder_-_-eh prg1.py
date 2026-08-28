import hashlib
def get_digests(data: str):
    byte_data = data.encode('utf-8')
    sha1=hashlib.sha1(byte_data).hexdigest()
    sha224=hashlib.sha224(byte_data).hexdigest()
    sha256=hashlib.sha256(byte_data).hexdigest()
    sha384=hashlib.sha384(byte_data).hexdigest()
    sha512=hashlib.sha512(byte_data).hexdigest()
    return {
    'SHA-1':sha1,
    'SHA-224':sha224,
    'SHA-256':sha256,
    'SHA-384':sha384,
    'SHA-512':sha512,
    }
if __name__=="__main__":
    input_data=input("enter the string to hash :")
    digests = get_digests(input_data)
    for algo,digest in digests.items():
        print(f"{algo} digest: {digest}")
