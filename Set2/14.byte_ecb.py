import random
from Crypto.Cipher import AES
import base64

def random_bytes(n):
    output = ""
    for i in range(n):
        tmp = random.randint(0,255)
        output=output+chr(tmp)
    return output
    
size=random.randint(20,100)
random_prefix = random_bytes(size)

block_length=16
def padding(text,k):
    req=k-len(text)%k
    if req!=k:
        for i in range(req):
            text=text+chr(req)
    else:
        for i in range(k):
            text=text+chr(k)
    return text 

key = random_bytes(block_length)

plain_text="divjot ko thandi drinks pasand hai"

def has_some_same_block(str1):
    for i in range(0,len(str1)-1,block_length):
        if (str1[i:i+block_length]==str1[i+block_length:i+2*block_length]):
            return True
    return False
    
def encryption_oracle(attacker_controlled):
    new_plain_text=random_prefix+attacker_controlled+plain_text
    new_plain_text=padding(new_plain_text,block_length)
    machine = AES.new(key, AES.MODE_ECB)
    output = machine.encrypt(new_plain_text)
    return str(output)
    
print size,len(plain_text),size+len(plain_text),len(encryption_oracle("")),len(encryption_oracle(""))-size-len(plain_text)
#############################

tmp_str1 = ""
tmp_str2 = "-"
tmp_ciph1 = encryption_oracle(tmp_str1)
tmp_ciph2 = encryption_oracle(tmp_str2)

for i in range(len(tmp_ciph1)):
    if (tmp_ciph1[i]!=tmp_ciph2[i]):
        prefix_block_len=i
        break;
for i in range(block_length):
    tmp_str = "-"*(2*block_length+i)
    tmp_ciph = encryption_oracle(tmp_str)
    if (has_some_same_block(tmp_ciph)):
        mod= block_length-i
        break
        
prefix_len = prefix_block_len + mod
###############################
extra = block_length-prefix_len%block_length
tmp_str1 = "-"*extra
tmp_ciph1 = encryption_oracle(tmp_str1)
unknown_length = len(tmp_ciph1)-prefix_len-extra

skip = prefix_len + extra

num_blocks = unknown_length/block_length
unknown_string = ""
for num in range(num_blocks-1):
    str1 = "A"*(extra+block_length-1)
    for i in range(block_length):
        test1 = encryption_oracle(str1)
        matching = dict()
        for j in range(255):
            str2 = str1 + unknown_string + chr(j)
            matching[encryption_oracle(str2)[skip+num*block_length:skip+num*block_length+block_length]] = str2
           
        tmp1 = test1[skip+num*block_length:skip+num*block_length+block_length]
        tmp2 = matching[tmp1]
        new_byte = tmp2[-1]
        unknown_string=unknown_string+new_byte
        str1 = str1[1:]
print unknown_string
