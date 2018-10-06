#!/usr/bin/env python3
# Cryptopals Set 1

import binascii
import base64
import itertools

# common letters PLUS space
FREQUENT_LETTERS = 'etaoinshrdlu '
FREQUENT_SET = set(FREQUENT_LETTERS)


def xor_buffers(byte_array_1, byte_array_2):
    rv = bytearray()
    for x, y in zip(byte_array_1, byte_array_2):
        rv.append(x ^ y)
    return rv


def xor_repeat(byte_array, key):
    rv = bytearray()
    for x, y in zip(byte_array, itertools.cycle(key)):
        rv.append(x ^ y)
    return rv


def xor_byte(byte_array, key):
    rv = bytearray()
    for x in byte_array:
        rv.append(x ^ key)
    return rv


def score_line(byte_array):
    rv = 0
    for x in byte_array:
        if ord('a') <= x <= ord('z') or ord('A') <= x <= ord('Z') or ord('0') <= x <= ord('9'):
            rv += 1
        if chr(x).upper() in FREQUENT_SET or chr(x).lower() in FREQUENT_SET:
            rv += 9
    return rv


def get_max_score(byte_array):
    m_score = 0
    m_byte = 0
    m_arr = ''
    for b in range(256):
        barr = xor_byte(byte_array, b)
        score = score_line(barr)
        if score > m_score:
            m_score = score
            m_byte = b
            m_arr = barr
    return m_score, m_byte, m_arr


def editdist(ba1, ba2):
    ed = 0
    for a, b in zip(ba1, ba2):
        ed += bin(a ^ b).count('1')
    return ed


# set 1 challenge 1

print('\nset 1 challenge 1')
str_1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
blob = binascii.a2b_hex(str_1)
benc = base64.b64encode(blob)
str_out = benc.decode()
print('{}'.format(str_out))


# set 1 challenge 2

print('\nset 1 challenge 2')
str_1 = '1c0111001f010100061a024b53535009181c'
str_2 = '686974207468652062756c6c277320657965'
blob1 = binascii.a2b_hex(str_1)
blob2 = binascii.a2b_hex(str_2)
barr = xor_buffers(blob1, blob2)
benc = binascii.b2a_hex(barr)
str_out = benc.decode()
print('{}'.format(str_out))


# set 1 challenge 3

print('\nset 1 challenge 3')
str_1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
benc = binascii.a2b_hex(str_1)
_, max_byte, max_arr = get_max_score(benc)
print('max byte {}'.format(max_byte))
print('decoded message:')
print('{}'.format(max_arr.decode()))


# set 1 challenge 4

print('\nset 1 challenge 4')
with open('04.txt') as f:
    max_score = 0
    max_byte = 0
    max_line = ''
    max_str = ''
    for line in f:
        line = line.rstrip()
        benc = binascii.a2b_hex(line)
        t_score, t_byte, t_arr = get_max_score(benc)
        if t_score > max_score:
            max_score = t_score
            max_byte = t_byte
            max_line = line
            max_arr = t_arr
f.close()
print('max byte {}'.format(max_byte))
print('max line {}'.format(max_line))
print('decoded message:')
print('{}'.format(max_arr.decode()))


# set 1 challenge 5

print('\nset 1 challenge 5')
str_1 = "Burning 'em, if you ain't quick and nimble\n\
I go crazy when I hear a cymbal"
key = 'ICE'
blobstr = str.encode(str_1)
blobkey = str.encode(key)
benc = xor_repeat(blobstr, blobkey)
hexs = binascii.b2a_hex(benc)
print('{}'.format(hexs.decode()))


# set 1 challenge 6

print('\nset 1 challenge 6')
# str_1 = "this is a test"
# str_2 = "wokka wokka!!!"
# ed = editdist(str.encode(str_1), str.encode(str_2))
# print('edit dist: {}'.format(ed))
with open('06.txt') as f:
    fenc = f.read().replace('\n', '')
f.close()
b64dec = base64.b64decode(fenc)
b64len = len(b64dec)
min_editdist = 8 * b64len       # all 8 bits are different for every byte
min_keysize = 0
# compare pairs of keysize-chunks of bytes, look for the lowest normalized edit distance
for keysize in range(1, 41):
    ed = 0
    numpairs = b64len // (2 * keysize)
    for c in range(0, numpairs * 2):
        c1 = b64dec[0:(c+1)*keysize]
        c2 = b64dec[(c+1)*keysize:(c+2)*keysize]
        ed += editdist(c1, c2)
    ed_norm = ed / (numpairs * keysize)
    if ed_norm < min_editdist:
        min_editdist = ed_norm
        min_keysize = keysize
print('min keysize {}, min normalized editdist {}'.format(min_keysize, min_editdist))
# transpose blocks and solve for each byte of the key
key = []
for i in range(0, min_keysize):
    block = [b64dec[x] for x in range(i, b64len, min_keysize)]
    _, max_byte, max_arr = get_max_score(block)
    key.append(max_byte)
key_s = [chr(x) for x in key]
key_s = ''.join(key_s)
print('key "{}"'.format(key_s))
dec = xor_repeat(b64dec, key)
print('decoded message:')
print('{}'.format(dec.decode()))


# set 1 challenge 7


# set 1 challenge 8
print('\nset 1 challenge 8')
with open('08.txt') as f:
    max_dupes = 0
    max_line = ''
    for line in f:
        line = line.rstrip()
# check line for repeated blocks
        chunks = []
        for i in range(0, len(line), 16):       # aes block size is 16
            chunks.append(line[i:i+16])
        num_dupes = len(chunks) - len(set(chunks))
        if num_dupes > max_dupes:
            max_dupes = num_dupes
            max_line = line
f.close()
print('max dupes: {}'.format(max_dupes))
print('line: {}'.format(max_line))
