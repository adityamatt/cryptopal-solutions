import base64
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

#def decrypt_cbc(key,iv,input_str):

key="YELLOW SUBMARINE"

#iv
iv="0000 0000 0000 0000"
iv=iv.replace(" ","")

fname="10.input"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content]

ciphertext=""

for msg in content:
    block_string=base64.b64decode(msg)
    ciphertext=ciphertext+block_string
    
#block length
k = 16

#Decypting function
machine = AES.new(key, AES.MODE_ECB)

prev = iv

n = len(ciphertext)
for i in range(0,n,16):
    cipherblock=ciphertext[i:i+16]
    plainblock=machine.decrypt(cipherblock)
    print strxor(plainblock,prev)
    prev=cipherblock

