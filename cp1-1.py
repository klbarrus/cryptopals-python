#!/usr/bin/env python
# Cryptopals Set 1 Challenge 1

import cpals
import base64

s_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# my own hexstring/base64 encoder
list_in = cpals.hexs_to_list(s_in)
b64_l = cpals.to_base64encoded(list_in)
b64_s = ''.join(b64_l)
print("{}".format(b64_s))

# using the base64 encoder
b64enc = base64.b64encode(str.encode(cpals.hexs_to_bstr(s_in)))
print("{}".format(b64enc))
