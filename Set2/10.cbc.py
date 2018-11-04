import base64

#def decrypt_cbc(key,iv,input_str):

key="YELLOW SUBMARINE"
iv="0000 0000 0000 0000"
iv=iv.replace(" ","")
fname="10.input"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
blocks=list()
content = [x.strip() for x in content]
block_string=""
for msg in content:
    print len(msg),msg
    block_string=block_string+base64.b64decode(msg)
index=0

