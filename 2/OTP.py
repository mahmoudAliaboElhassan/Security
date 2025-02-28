import os
def generate_key(length):
    return os.urandom(length)
def OTP_encrypt(plainText):
    textBytes=plainText.encode("UTF-8")
    key=generate_key(len(textBytes))
    cipherText=[p^k for p,k in zip(textBytes,key)]
    return  (cipherText),key

def OTP_decrypt(cipherText,key):
    plaintext=[p^k for p,k in zip(cipherText,key)]
    # print(plaintext)
    return bytes(plaintext).decode()
    # return bytes(plaintext) # b'hello everyone'

plaintext="hello everyone"
ciphertext,key=OTP_encrypt(plaintext)
print(ciphertext)
print(OTP_decrypt(ciphertext,key))

