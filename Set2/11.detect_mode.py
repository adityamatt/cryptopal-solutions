import random
from Crypto.Cipher import AES


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
    
def encryption_oracle(plain_text):
    key = random_bytes(16)
    prepend=random.randint(5,10)
    append=random.randint(5,10)
    new_plain_text=random_bytes(prepend)+plain_text+random_bytes(append)
    new_plain_text=padding(new_plain_text,16)
    choice = random.randint(0,1)
    
    if choice==0:
        #ECB
        print "ENCRYPTION MODE:ECB"
        machine = AES.new(key, AES.MODE_ECB)
    else:
        #CBC
        print "ENCRYPTION MODE:CBC"
        machine = AES.new(key, AES.MODE_CBC,random_bytes(16))
    output = machine.encrypt(new_plain_text)
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
    
mode=detect_mode(encryption_oracle)
print "DETECTED MODE :",mode
