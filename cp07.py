#!/usr/bin/env python3
# cryptopals set 1 challenge 7

import binascii
import cpals_aes


# from FIPS 197, example key in A.1, example input Appendix B
aes_input_text =  '32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34'
cipher_key_text = '2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c'

# remove spaces that were added for readability
aes_input_text = aes_input_text.replace(' ', '')
cipher_key_text = cipher_key_text.replace(' ', '')
aes_key = binascii.a2b_hex(cipher_key_text)
aes_input = binascii.a2b_hex(aes_input_text)

print('input')
print('{}'.format(binascii.b2a_hex(aes_input)))
print('key')
print('{}'.format(binascii.b2a_hex(aes_key)))
print('')

enc_output = cpals_aes.encrypt(aes_input, aes_key)
enc_output_text = binascii.b2a_hex(enc_output)

print('output (encryption)')
print('{}'.format(enc_output_text))
print('')

dec_output = cpals_aes.decrypt(enc_output, aes_key)
dec_output_text = binascii.b2a_hex(dec_output)

print('output (decryption)')
print('{}'.format(dec_output_text))
print('')
