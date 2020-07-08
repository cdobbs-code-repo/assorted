def ascii_to_letter(foo):
    low_lett = "abcdefghijklmnopqrstuvwxyz"
    upp_lett = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #ADD comma and period as well
    if foo == 44:
        return ","
    if foo == 46:
        return "."
    if foo == 32:
        return " "
    if foo > 96 and foo < 123:
        return low_lett[foo - 97]
    if foo > 64 and foo < 91:
        return upp_lett[foo - 65]
    #otherwise
    return "*"

#hex to dec conversion
def hex_to_dec(foo):
    letts = " ABCDEF"
    if foo[0] in letts:
        num1 = 9 + letts.index(foo[0])
    else:
        num1 = int(foo[0])
    if foo[1] in letts:
        num0 = 9 + letts.index(foo[1])
    else:
        num0 = int(foo[1])
    return num1*16 + num0


#note: bitwise xor with decimal values is a ^ b

#store encrypted message in a list
myfile = open("C:/Users/cdobb/Desktop/Python_stuff/encrypted_message_vigenere.txt")
message = myfile.read()
myfile.close() 

#put in list with each ascii hex (2 byte) letter
message_bins = []
for i in range(0,len(message),2):
    message_bins.append(hex_to_dec(message[i]+message[i+1]))

#print(message_bins)
mymessage = ""
cipher = [186,31,145,178,83,205,62]
myiter = 0
for x in message_bins:
    mymessage += ascii_to_letter(x ^ cipher[myiter%7])
    myiter += 1

print(mymessage)