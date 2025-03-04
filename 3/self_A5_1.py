def A51_encrypt(plainText,key):
    plainText_bits=[]
    for ch in plainText:
        bits=f"{ord(ch):08b}"
        print("bits",bits)
        plainText_bits.extend(int(i) for i in bits)
    R1=[int (i) for i  in bin(key&0x7FFF)[2:].zfill(19)]
    R2=[int (i) for i in bin((key>>19)&0x3FFFFF)[2:].zfill(22)]
    R3=[int (i) for i in bin((key>>41)&0x7FFFFF)[2:].zfill(23)]
    print("plainText",plainText_bits)
    key_stream=[]
    for i in range(len(plainText_bits)):
        majority=(R1[8]+R2[10]+R3[10])>=2
        if(R1[8]==majority):
            newBit=R1[13]^R1[16]^R1[17]^R1[18]
            R1=[newBit]+R1[:-1]
        if(R2[10]==majority):
            newBit=R2[20]^R2[21]
            R2=[newBit]+R2[:-1]
        if(R3[10]==majority):
            newBit=R3[7]^R3[20]^R3[21]^R3[22]
            R3=[newBit]+R3[:-1]
        key_stream.append(R1[18]^R2[21]^R3[22])
        
        
    cipherText=[]
    for i,k in zip(plainText_bits,key_stream):
        cipherText.append(i^k)
    print("cipherText from fun",cipherText)
    cipher_text_chars=[]
    for i in range(0, len(cipherText), 8):
        x=map(str,cipherText[i:i+8])
        
        # map(str, ...) converts each bit (which is an integer) to a string.
        # Bits: [0, 1, 0, 0, 1, 0, 0, 0]
        # After map: ['0', '1', '0', '0', '1', '0', '0', '0']
        x_int=int(''.join(x),2)
        # ['0', '1', '0', '0', '1', '0', '0', '0'] → '01001000'
        # Binary '01001000' → Decimal 72
        cipher_text_chars.append(chr(x_int))
        # Converts the decimal integer to its corresponding ASCII character using chr() and appends it to the cipher_text_chars list.
    return ''.join(cipher_text_chars)


def decrypt(ciphertext, key):
    """Decrypt ciphertext using A5/1 (same as encryption)."""
    return A51_encrypt(ciphertext, key)  # XORing twice cancels out encryption

import random
# Example Usage
key = random.getrandbits(64)  # 64-bit key
plaintext = "HELLO"
ciphertext = A51_encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted: ", decrypted_text)





# x=map(str,cipher[i:i+8])
# x_int =int("".join(x),2)
# cipher_chars.append(chr(x_int))
# return "".join(cipher_chars)