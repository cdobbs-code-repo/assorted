import bin_hex_ascii_converter as myascii

def list_to_string(foo):
    bar = ""
    for x in foo:
        bar += x
    return bar


foo = "JR4YFw8YLwA7Jx0mCRsaGBsMKhwSLwMdLhsBMC0YHBgwMwcBMBcmFBsfIjAHKxMVHBEBIAoXfA8="
x = ""
for bar in foo:
    x += myascii.b64_to_binary(bar)
#print(x)

xornum = [67,114,121,112,116,111,71,111,50]
for temp in range(0,256):
    xornum[8] = temp
    msg_bin = ""
    count = 0
    for i in range(0, len(x)-4, 8):
        msg_bin += myascii.ascii_to_letter(myascii.hex_to_dec(myascii.bin_to_hex(x[i:i+4]) + myascii.bin_to_hex(x[i+4:i+8])) ^ xornum[count%len(xornum)] )
        count += 1

    if msg_bin[17] == "h":
        print(xornum)
        print(msg_bin)
# if "flag" in msg_bin:
#     print(xornum)
#     print(count-1)
#     print(xornum[(count-1)%len(xornum)])
#     print(msg_bin)

# for i in range(0,256):
#     bar = foo
#     bar2 = ""
#     for x in bar:
#         #temp = ord(x)
#         temp2 = x ^ i
#         bar2 += myascii.ascii_to_letter(temp2)
# #print(bar)
#     print(bar2)

