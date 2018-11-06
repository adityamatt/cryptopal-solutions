def valid_padding(str1):
    n = len(str1)
    if ord(str1[-1])>15:
        return str1
    padding = ord(str1[-1])
    print n,padding
    if padding>n:
        print "INVALID PADDING"
        return str1
    for i in range(1,padding+1):
#        print ord(str1[-1]),padding
        if ord(str1[-i])!=padding:
            print "INVALID PADDING"
            return str1
    return str1[0:n-padding]

a= "ICE ICE BABY\x01\x02\x03\x04"
print a
print valid_padding(a)
