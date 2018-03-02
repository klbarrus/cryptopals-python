#!/usr/bin/env python
# Cryptopals Set 1 Challenge 4

import cpals

maxscore = 0
maxbyte = 0
maxline = []
with open("./4.txt") as f:
    for line in f:
        he = cpals.hexs_to_intl(line.rstrip())
        score,byte = cpals.xor_loop(he)
        if score > maxscore:
            maxscore = score
            maxbyte = byte
            maxline = he
f.close()
print("maxscore {}, byte {}".format(maxscore,maxbyte))
m = cpals.xor(maxline,maxbyte)
d1 = cpals.to_string(m)
print("{}".format(d1))
