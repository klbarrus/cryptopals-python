#!/usr/bin/env python3
# cryptopals set 1 challenge 3

import cpals
import binascii


str_in1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

blob1 = binascii.a2b_hex(str_in1)
_, maxbyte = cpals.xor_max(blob1)
print('maxscore with byte {}'.format(maxbyte))

str_dec = cpals.xor_byte(blob1, maxbyte)
hex_out = binascii.b2a_hex(str_dec).decode()
str_out = bytes.fromhex(hex_out).decode('utf-8')
print('{}'.format(str_out))
