from Crypto.Cipher import AES
import itertools
import binascii



def data(filename):
    f = open(filename, 'r')
    output=list()
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        line=line.decode("hex")
        output.append(line)
    return output

def unique(line):
    block_size= 16
    blocks=list()
    n = len(line)
    if n%block_size!=0:
        print "Invalid Encryption EBC"
        return 0
    for i in range(0,n,block_size):
        tmp=line[i:i+block_size]
        blocks.append(tmp)
    same=0
    num_blocks=len(blocks)
    for i in range(num_blocks):
        for j in range(i+1,num_blocks):
            if i!=j and blocks[i]==blocks[j]:
                same=same+1
    return same

fname="8.input"
lines = data(fname)
lineNumber = 1
for l in lines:
    if (unique(l)>0):
        print "EBC encrypted line:",lineNumber
    lineNumber=lineNumber+1
