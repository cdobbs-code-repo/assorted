
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


#store encrypted message in a list
myfile = open("C:/Users/cdobb/Desktop/Python_stuff/encrypted_message_vigenere.txt")
message = myfile.read()
myfile.close() 

#put in list with each ascii hex (2 byte) letter
message_bins = []
for i in range(0,len(message),2):
    message_bins.append(message[i]+message[i+1])


# First, we find N, the length of the cipher
## we must guess N and check if Nth char freqs are english letter freqs in permuted order 
### * the sum squared should be much greater than 1/256 see notes *

# our values will be ascii hex and thus 0x00 to 0xFF --> 0 to 255
qi2_vals = []

N = 7

for i in range(0,N):
    bin_list = [0]*256

    while i < len(message_bins):
        bin_list[hex_to_dec(message_bins[i])] += 1/256
        i += N

    qi2 = 0
    for x in bin_list: 
        qi2 += x**2
    qi2_vals.append(qi2)

print(sum(qi2_vals))