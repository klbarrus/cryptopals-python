#!/usr/bin/env python
# Cryptopals Set 1 Challenge 5

import cpals

m = "Burning 'em, if you ain't quick and nimble\n\
I go crazy when I hear a cymbal"
k = "ICE"
ct = cpals.to_hexstring(cpals.xor_repeatkey(cpals.to_bytes(m),cpals.to_bytes(k)))
print("{}".format(ct))
