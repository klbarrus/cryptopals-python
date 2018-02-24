#!/usr/bin/env python
# Cryptopals utility functions

from itertools import zip_longest

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def hexstring_to_numlist(hs):
    nl = []
    for ch in hs:
        num = 0
        if '0' <= ch and ch <= '9':
            num = int(ch)
        elif 'a' <= ch and ch <= 'f':
            num = ord(ch) - ord('a') + 10
        elif 'A' <= ch and ch <= 'F':
            num = ord(ch) - ord('A') + 10
        nl.append(num)
    return nl

def numlist_to_b64list(nl):
    b64 = []
    for a,b,c in grouper(nl, 3, 0):
        i1 = (a << 2) + ((b & 0xC) >> 2)
        i2 = ((b & 0x3) << 4) + c
        b64.append(BASE64[i1])
        b64.append(BASE64[i2])
    return b64

def fixed_xor(l1, l2):
    res = []
    for a,b in zip(l1,l2):
        res.append(a^b)
    return res
