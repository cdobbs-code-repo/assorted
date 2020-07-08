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


# C = M ^ K = M XOR K

c1 = "BB3A65F6F0034FA957F6A767699CE7FABA855AFB4F2B520AEAD612944A801E"
c2 = "BA7F24F2A35357A05CB8A16762C5A6AAAC924AE6447F0608A3D11388569A1E"
c3 = "A67261BBB30651BA5CF6BA297ED0E7B4E9894AA95E300247F0C0028F409A1E"
c4 = "A57261F5F0004BA74CF4AA2979D9A6B7AC854DA95E305203EC8515954C9D0F"
c5 = "BB3A70F3B91D48E84DF0AB702ECFEEB5BC8C5DA94C301E0BECD241954C831E"
c6 = "A6726DE8F01A50E849EDBC6C7C9CF2B2A88E19FD423E0647ECCB04DD4C9D1E"
c7 = "BC7570BBBF1D46E85AF9AA6C7A9CEFA9E9825CFD5E3A0047F7CD009305A71E"

c1_bins = []
for i in range(0,len(c1),2):
    c1_bins.append(hex_to_dec(c1[i]+c1[i+1]))

c2_bins = []
for i in range(0,len(c2),2):
    c2_bins.append(hex_to_dec(c2[i]+c2[i+1]))

c3_bins = []
for i in range(0,len(c3),2):
    c3_bins.append(hex_to_dec(c3[i]+c3[i+1]))

c4_bins = []
for i in range(0,len(c4),2):
    c4_bins.append(hex_to_dec(c4[i]+c4[i+1]))

c5_bins = []
for i in range(0,len(c5),2):
    c5_bins.append(hex_to_dec(c5[i]+c5[i+1]))

c6_bins = []
for i in range(0,len(c6),2):
    c6_bins.append(hex_to_dec(c6[i]+c6[i+1]))

c7_bins = []
for i in range(0,len(c7),2):
    c7_bins.append(hex_to_dec(c7[i]+c7[i+1]))

myout = []
count = 0
for x in c5_bins:
    myout.append(int(x) ^ int(c7_bins[count]))
    count += 1



