import random
from Crypto.Cipher import AES
import base64


def random_bytes(n):
    output = ""
    for i in range(n):
        tmp = random.randint(0,255)
        output=output+chr(tmp)
    return output
    

    
def detect_mode(encryption_oracle):
    test = ""
    for i in range(80):
        test=test+"0"
    encrypted = encryption_oracle(test)
    tmp = len(encrypted)
    for i in range(0,tmp-16,16):
        if encrypted[i:i+16]==encrypted[i+16:i+32]:
            return "ECB"
    return "CBC"

def padding(text,k):
    req=k-len(text)%k
    if req!=k:
        for i in range(req):
            text=text+chr(req)
    else:
        for i in range(k):
            text=text+chr(k)
    return text 

#Global Variables
appending= "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
to_append=base64.b64decode(appending)

#print to_append

key = random_bytes(16)


def encryption_oracle(plain_text):
    new_plain_text=plain_text+to_append
    new_plain_text=padding(new_plain_text,16)
    machine = AES.new(key, AES.MODE_ECB)
    output = machine.encrypt(new_plain_text)
    return str(output)
    
#Finding Block length 16 pata hai vasie bhi
str1 = ""
test1 = encryption_oracle(str1)
prev_len=len(test1)
unknown_length = prev_len
test=dict()
for i in range(500):
    str1 = str1 + "A"
    test1 = encryption_oracle(str1)
    if len(test1)>prev_len:
        block_length = len(test1)-prev_len
        break

mode = detect_mode(encryption_oracle)
print "Mode DETECTED",mode

#################

unknown_string=""
num_blocks = unknown_length/block_length
for num in range(num_blocks-1):
    str1 = "A"*15
    for i in range(block_length):
        test1 = encryption_oracle(str1)
        
        matching = dict()
        for j in range(255):
            str2 = str1 + unknown_string + chr(j)
            matching[encryption_oracle(str2)[num*block_length:num*block_length+block_length]] = str2
        tmp1 = test1[num*block_length:num*block_length+block_length]
        tmp2 = matching[tmp1]
        new_byte = tmp2[-1]
        unknown_string=unknown_string+new_byte
        str1 = str1[1:]
print unknown_string
        

        
        

