#!/usr/bin/env python3
# cryptopals set 1 challenge 5

import cpals
import binascii


m = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
k = b'ICE'

enc = cpals.xor_repeatkey(m, k)
str_out = binascii.b2a_hex(enc).decode()
print('{}'.format(str_out))
