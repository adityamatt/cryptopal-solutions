from Crypto.Cipher import AES
import base64

fname="7.input"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
key="YELLOW SUBMARINE"
output=""
decipher = AES.new(key, AES.MODE_ECB)
for msg in content:
    msg=base64.b64decode(msg)
    output=output+msg
print(decipher.decrypt(output))
