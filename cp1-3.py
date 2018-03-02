#!/usr/bin/env python
# Cryptopals Set 1 Challege 3

import cpals

s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
l1 = cpals.hexs_to_intl(s1)
maxscore,maxbyte = cpals.xor_loop(l1)
print("maxscore {}, byte {}".format(maxscore, maxbyte))
m = cpals.xor(l1, maxbyte)
d1 = cpals.to_string(m)
print("{}".format(d1))
