#!/usr/bin/env python
# Cryptopals Set 1 Challenge 6

import cpals
import base64

#ed = cpals.calc_editdist(str.encode("this is a test"),str.encode("wokka wokka!!!"))
#print("{}".format(ed))

with open("./6.txt") as f:
    enc = f.read().replace('\n','')
f.close()
b64dec = base64.b64decode(enc)
b64len = len(b64dec)
mined = 8*b64len # all 8 bits are different for every byte
minks = 0
for ks in range(1, 41):
    ed = 0
# compare pairs of keysize-chunks of bytes, looking for the lowest normalized edit distance    
    numpairs = b64len//(2*ks)
    for c in range(0,numpairs,2):
        c1 = b64dec[0:(c+1)*ks]
        c2 = b64dec[(c+1)*ks:(c+2)*ks]
        ed += cpals.calc_editdist(c1,c2)
    ned = ed / (numpairs * ks)
    if ned < mined:
        mined = ned
        minks = ks
#    print("keysize {}, normalized edit distance {}".format(ks,ned))
print("min ks {}, min ed {}".format(minks, mined))

# transpose blocks and solve for individual byte of key
key = []
for i in range(0,minks):
    block = [b64dec[x] for x in range(i,b64len,minks)]
    ms, mb = cpals.xor_loop(block)
    key.append(mb)
print("key: {}".format(cpals.to_string(key)))

# decrypt original message
dm = cpals.xor_repeatkey(b64dec, key)
print("message:")
print("{}".format(cpals.to_string(dm)))
