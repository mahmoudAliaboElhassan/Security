def vig_encrypt(plainText,key):
    cipherText=""
    for i,ch in enumerate(plainText):
        if ch.isalpha():
            key_ind=i%len(key)
            baseK=ord("A") if key[key_ind].isupper() else ord("a")
            shiftVal=ord(key[key_ind])-baseK
            base=ord("A")if ch.isupper() else ord("a")
            cipherText+=chr(base+(ord(ch)-base+shiftVal+26)%26)
        else:
            cipherText+=ch
    return cipherText


key="ali"
text="Ramy & ,"
ciphertext=vig_encrypt(text,key)
print("ciphertext:",ciphertext)





def vig_decrypt(cipherText,key):
    plainText=""
    for i,ch in enumerate(cipherText):
        if ch.isalpha():
            key_ind=i%len(key)
            baseK=ord("A") if key[key_ind].isupper()else ord("a")
            shiftVal=ord(key[key_ind])-baseK
            base=ord("A") if ch.isupper()else ord("a")
            plainText+=chr(base+(ord(ch)-base-shiftVal+26)%26)
        else:
            plainText+=ch
    return plainText
    

key="ali"
text="Rluy & ,"
plainText=vig_decrypt(text,key)
print("plainText:",plainText)