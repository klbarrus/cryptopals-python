#!/usr/bin/env python
# Cryptopals Set 1 Challenge 5

import cpals

m = "Burning 'em, if you ain't quick and nimble\n\
I go crazy when I hear a cymbal"
k = "ICE"
me = str.encode(m)
ke = str.encode(k)
ct = cpals.to_hexstring(cpals.xor_repeatkey(me,ke))
print("{}".format(ct))
