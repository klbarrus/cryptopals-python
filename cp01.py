#!/usr/bin/env python3
# cryptopals set 1 challenge 1

import cpals
import binascii
import base64


str_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# my own hexstring/base64 encoder
list_in = cpals.hexs_to_list(str_input)
b64_l = cpals.to_base64encoded(list_in)
b64_s = ''.join(b64_l)
print('{}'.format(b64_s))

# using the base64 encoder
blob = binascii.a2b_hex(str_input)
benc = base64.b64encode(blob)
str_out = benc.decode()
print('{}'.format(str_out))
