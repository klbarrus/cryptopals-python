#!/usr/bin/env python
# Cryptopals Set 1 Challenge 2

import cpals

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

l1 = cpals.hexstring_to_numlist(s1)
l2 = cpals.hexstring_to_numlist(s2)
xor_l = cpals.fixed_xor(l1,l2)
xor_s = ''.join([str(x) for x in xor_l])
print("{}".format(xor_s))