#!/usr/bin/env python3
# cryptopals set 1 challenge 2

import cpals
import binascii


str_in1 = '1c0111001f010100061a024b53535009181c'
str_in2 = '686974207468652062756c6c277320657965'

blob1 = binascii.a2b_hex(str_in1)
blob2 = binascii.a2b_hex(str_in2)
barr = cpals.xor_bytearray(blob1, blob2)
benc = binascii.b2a_hex(barr)
str_out = benc.decode()
print('{}'.format(str_out))
