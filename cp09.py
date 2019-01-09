#!/usr/bin/env python3
# cryptopals set 1 challenge 9

import cpals


str_in = 'YELLOW SUBMARINE'
str_b = bytes(str_in, 'utf-8')
padded_b = cpals.pkcs7_padding(str_b, 20)
print('{}'.format(padded_b))
padded_str = padded_b.decode('utf-8')
print('{}'.format(padded_str))
