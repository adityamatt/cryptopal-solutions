input_str="YELLOW SUBMARINE"
input_length=20
input_byte=len(input_str)
padding=input_length-input_byte%input_length
print padding
output=input_str
for i in range(padding):
    output=output+hex((padding))
print (output)

