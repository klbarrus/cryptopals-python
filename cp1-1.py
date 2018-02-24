#!/usr/bin/env python
# Cryptopals Set 1 Challenge 1

import cpals

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
nl = cpals.hexstring_to_numlist(hex_string)
b64_l = cpals.numlist_to_b64list(nl)
b64_s = ''.join(b64_l)
print("{}".format(b64_s))
