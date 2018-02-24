#!/usr/bin/env python
# Cryptopals Set 1 Challege 3

import cpals

s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
l1 = cpals.from_hexencoded(s1)
maxscore = 0
maxbyte = 0
for i in range(256):
    m = cpals.xor_encrypt(l1,i)
    score = cpals.score(m)
    if score > maxscore:
        maxscore = score
        maxbyte = i
print("maxscore {}, byte {}".format(maxscore, maxbyte))
m = cpals.xor_encrypt(l1, maxbyte)
d1 = cpals.to_string(m)
print("{}".format(d1))