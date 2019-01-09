#!/usr/bin/env python3
# cryptopals set 1 challenge 4

import cpals
import binascii


with open('./04.txt') as f:
    lines = [line.rstrip() for line in f]
f.close()

maxscore = 0
maxbyte = 0
maxline = ''
for line in lines:
    blob_in = binascii.a2b_hex(line)
    score, byte = cpals.xor_max(blob_in)
    if score > maxscore:
        maxscore = score
        maxbyte = byte
        maxline = line
print('maxscore {}, byte {}'.format(maxscore, maxbyte))
print('{}'.format(maxline))
print('')

blob_in = binascii.a2b_hex(maxline)
str_dec = cpals.xor_byte(blob_in, maxbyte)
hex_out = binascii.b2a_hex(str_dec).decode()
str_out = bytes.fromhex(hex_out).decode('utf-8')
print('{}'.format(str_out))
