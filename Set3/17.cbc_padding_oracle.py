import random
from Crypto.Cipher import AES
import base64
from Crypto.Util.strxor import strxor

plain_texts =["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
"MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
"MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
"MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
"MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
"MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
"MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]
    
def is_valid_padding(str1):
    n = len(str1)
    last_char = ord(str1[-1])
    if last_char>16:
        return True
    if last_char==0 or str1[-last_char:]!=chr(last_char)*last_char:
        return False
    return True

def remove_padding(str1):
    padding = ord(str1[-1])
    n = len(str1)
    return str1[0:n-padding]

def random_bytes(n):
    output = ""
    for i in range(n):
        tmp = random.randint(0,255)
        output=output+chr(tmp)
    return output

def padding(text,k):
    req=k-len(text)%k
    if req!=k:
        for i in range(req):
            text=text+chr(req)
    else:
        for i in range(k):
            text=text+chr(k)
    return text 
    
block_length = 16
key = random_bytes(block_length)

def AES_encrypt(text):
    text = padding(text,block_length)
#    text = text + '\x16'*16
    iv = random_bytes(block_length)
    machine = AES.new(key, AES.MODE_CBC,iv)
    cipher = machine.encrypt(text)
    return iv,cipher

def AES_decrypt(iv,cipher):
    machine = AES.new(key, AES.MODE_CBC,iv)
    return machine.decrypt(cipher)
    
def challenger():
    index = random.randint(0,len(plain_texts)-1)
#    index =0
    plain_text = plain_texts[index]
    plain_text = base64.b64decode(plain_text)
    return AES_encrypt(plain_text)

def oracle(iv,ciphertext):
    machine = AES.new(key, AES.MODE_ECB)
    prev = iv
    n = len(ciphertext)
    output=""
    for i in range(0,n,16):
        cipherblock=ciphertext[i:i+16]
        plainblock = machine.decrypt(cipherblock)
        plainblock = strxor(plainblock,prev)
        output = output+plainblock
        prev=cipherblock
    print output
    if is_valid_padding(output):
        return True
    else:
        return False
        
IV,CIPHER=challenger()
#print CIPHER
print "---------------------"
#########################
print oracle(IV,CIPHER)
