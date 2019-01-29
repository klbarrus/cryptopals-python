#!/usr/bin/env python3
# cryptopals challenge 10

import binascii
import base64
import cpals_aes


cpals_input_text = 'YELLOW SUBMARINE'
cpals_key = cpals_input_text.encode('utf-8')

with open('./10.txt')as f:
    fc = f.read().replace('\n', '')
f.close()

fc_b64dec = base64.b64decode(fc)
dec_output = cpals_aes.decrypt_cbc(fc_b64dec, cpals_key)
dec_output_text = binascii.b2a_hex(dec_output)

print('output (decryption)')
print('{}'.format(dec_output))
print('')

enc_output = cpals_aes.encrypt_cbc(dec_output, cpals_key)

if enc_output == fc_b64dec:
    print('encryption matches, pass!')
else:
    print('encryption mismatch, fail')
