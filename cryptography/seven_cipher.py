

def ascii_to_letter(foo):
    low_lett = "abcdefghijklmnopqrstuvwxyz"
    upp_lett = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #ADD comma and period as well
    if foo == 44:
        return ","
    if foo == 46:
        return "."
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
myfile = open("C:/Users/cdobb/Desktop/Python_stuff/encrypted_message_vigenere2.txt")
message = myfile.read()
myfile.close() 

#put in list with each ascii hex (2 byte) letter
message_bins = []
for i in range(0,len(message),2):
    message_bins.append(message[i]+message[i+1])


#now assuming N letter cipher, we want to try 32 to 127 (ascii letters)
# as ciphers and find 'most likely' candidate
# **per each N spaced letters (don't mix up)**

low_lett = "abcdefghijklmnopqrstuvwxyz"

N = 31

ciph_bins = [None]*256
for ciph in range(0,256):
    i = 5
    letter_bin = [0]*26
    ciphbool = True
    while i < len(message_bins) and ciphbool:
        temp = hex_to_dec(message_bins[i]) 
        temp = temp ^ ciph #this is our decimal ascii letter
        if temp < 32 or temp > 127:
            ciphbool = False
        if ascii_to_letter(temp) in low_lett:
            letter_bin[low_lett.index(ascii_to_letter(temp))] += 1/256
        i += N
    if ciphbool == False:
        ciph_bins[ciph] = 0
    else:
        qi2 = 0
        for x in letter_bin:
            qi2 += x**2
        ciph_bins[ciph] = qi2

#print(ciph_bins)
#ciph_bins.pop(ciph_bins.index(max(ciph_bins)))
print(ciph_bins.index(max(ciph_bins)))

#ciph_conv = []
#mycount = 0
#for x in ciph_bins:
#    if x:
#        ciph_conv.append(ascii_to_letter(mycount))
#    else:
#        ciph_conv.append("--")
#    mycount += 1
#
#print(ciph_conv)

