import random
from Crypto.Cipher import AES
import base64
from Crypto.Util.strxor import strxor
import struct

nonce=0
block_length = 16

input_file = "./20.input"

#Plain texts
plain_texts = open(input_file).read().splitlines()
for i in range(len(plain_texts)):
    plain_texts[i] = base64.b64decode(plain_texts[i])


def random_bytes(n):
    output = ""
    for i in range(n):
        tmp = random.randint(0,255)
        output=output+chr(tmp)
    return output   
    
def little(inp):
    a= str(struct.pack("<q",inp))
    return a


def encrypt(nonce,plain_text,key):
    key_len = len(plain_text)
    key_stream = ""
    counter = 0
    machine = AES.new(key,AES.MODE_ECB)
    while (len(key_stream)<len(plain_text)):
        key_block = b''
        key_block = key_block+little(nonce)+little(counter)
        key_block = machine.encrypt(key_block)
        key_stream = key_stream+key_block
        counter = counter + 1
    key_stream = key_stream[:key_len]
    return strxor(key_stream,plain_text)

def find_xor_key(input_):
    n = len(input_)
    freq = dict()
    for i in range(n):
        tmp =strxor(input_[i]," ")
        if tmp in freq:
            freq[tmp] += 1
        else:
            freq[tmp]  = 1

    for tmp_key in freq:
        c = tmp_key
        f = freq[tmp_key]
        break
        
    for tmp_key in freq:
        if freq[tmp_key] > f:
            c = tmp_key
            f= freq[tmp_key]
    return c
        
    
def break_(cipher,key_len):
    n = len(cipher)
    keystream = ""
    for i in range(key_len):
        basic = ""
        j = i
        while (j<n):
            basic = basic + cipher[j]
            j = j+key_len;
        keystream += find_xor_key(basic)
    return keystream
    
cipher_texts = list()
key = random_bytes(block_length)

for p in plain_texts:
    cipher_texts.append(encrypt(nonce,p,key))
    
##################### Attacking
min_len = min([len(p) for p in cipher_texts])
max_len = max([len(p) for p in cipher_texts])

concat_cipher = ""
for i in range(len(cipher_texts)):
    cipher_texts[i] = cipher_texts[i][:min_len]
    concat_cipher = concat_cipher + cipher_texts[i]

key_len = min_len

#Breaking repeated key XOR
key_stream = break_(concat_cipher,key_len)

for i in range(0,len(concat_cipher),key_len):
    tmp = strxor(concat_cipher[i:i+key_len],key_stream)
    print tmp
