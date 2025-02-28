def double_transposition_encrypt(plainText,row,col,perRow,perCol):
    cipherText= []
    for i in range(row):
        cipherText.append([])
        for j in range(col):
            cipherText[i].append(".")
    for i in range(row):
        for j in range(col):
            cipherText[i][j]=plainText[perRow[i]-1][perCol[j]-1]
            # as array is zero indexing and
            # and permuation starts with one
    return cipherText



perR=[3,2,1]
perC=[4,2,1,3]
plaintext=[['a','t','t','a'],['c','k','a','t'],['d','a','w','n']]
rows=len(plaintext)
cols=len(plaintext[0])
cipher=double_transposition_encrypt(plaintext,rows,cols,perR,perC)
print("cipher: ",cipher)





def double_transposition_decrypt(cipherText,row,col,perRow,perCol):
    plaintext=[]
    for i in range(row):
        plaintext.append([])
        for j in range(col):
            plaintext[i].append(".")
    for i in range(row):
        for j in range(col):
            plaintext[perRow[i]-1][perCol[j]-1]=cipherText[i][j]
    return plaintext


plain=double_transposition_decrypt(cipher,rows,cols,perR,perC)
print("plain: ",plain)
