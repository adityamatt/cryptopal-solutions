def valid_padding(str1):
    n = len(str1)
    last_char = ord(str1[-1])
    if last_char==0 or str1[-last_char:]!=chr(last_char)*last_char:
        raise ValueError("Bad padding")
    return str1[0:n-last_char]
    
a= "ICE ICE BAB\x04\x04\x04\x04"
print a
print valid_padding(a)
