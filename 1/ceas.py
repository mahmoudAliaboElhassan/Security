# ceaser cipher
def ceaser_encrypt(plainText,shift):
    cipher_text=""
    for ch in plainText:
        if ch.isalpha():
            base=ord("A") if ch.isupper() else ord("a")
            cipher_text+=chr(base+(ord(ch)-base+shift+26)%26)
        else:
            cipher_text+=ch
    return cipher_text


plain_txt="Ramy"
shift=3
chiper_txt=ceaser_encrypt(plain_txt,shift)
print("Cipher Text",chiper_txt)







def ceaser_decrypt(cipher_text,shift):
    plain_txt=""
    for ch in cipher_text:
        if ch.isalpha():
            base=ord("A") if ch.isupper() else ord("a")
            plain_txt+=chr(base+(ord(ch)-base-shift+26)%26)
        else:
            plain_txt+=ch

    return plain_txt

cipher="Udpb"
plain=ceaser_decrypt(cipher,shift)
print("Plain text ",plain )