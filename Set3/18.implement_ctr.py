import random
from Crypto.Cipher import AES
import base64
from Crypto.Util.strxor import strxor
import struct

string1 = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
key = "YELLOW SUBMARINE"
nonce=0
block_length = 16

def reverse(inp):
    return "".join(reversed(inp))
   
    
def little(inp):
    a= str(struct.pack("<q",inp))
    return a


def encrypt(nonce,plain_text):
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
    
print encrypt(nonce,base64.b64decode(string1))
