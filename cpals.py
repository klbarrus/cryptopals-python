#!/usr/bin/env python
# Cryptopals utility functions

from itertools import zip_longest

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def from_hexstring(s):
    res = []
    for x in s:
        num = 0
        if '0' <= x and x <= '9':
            num = int(x)
        elif 'a' <= x and x <= 'f':
            num = ord(x) - ord('a') + 10
        elif 'A' <= x and x <= 'F':
            num = ord(x) - ord('A') + 10
        res.append(num)
    return res

def from_hexencoded(s):
    res = []
    for ha,hb in grouper(s,2,0):
        a = hexdigit_to_dec(ha)
        b = hexdigit_to_dec(hb)
        res.append(a*16+b)
    return res

def to_base64encoded(s):
    res = []
    for a,b,c in grouper(s, 3, 0):
        x = (a << 2) + ((b & 0xC) >> 2)
        y = ((b & 0x3) << 4) + c
        res.append(BASE64[x])
        res.append(BASE64[y])
    return res

def fixed_xor(s1, s2):
    res = []
    for a,b in zip(s1,s2):
        res.append(a^b)
    return res

def xor_encrypt(s1, v):
    res = [x^v for x in s1]
    return res

def score(s):
    score = 0
    for x in s:
        xo = chr(x)
        if 'a' <= xo and xo <= 'z':
            score += 1
        elif 'A' <= xo and xo <= 'Z':
            score += 1
        
        if xo == 'E' or xo == 'e' or \
           xo == 'T' or xo == 't' or \
           xo == 'A' or xo == 'a' or \
           xo == 'O' or xo == 'o' or \
           xo == 'I' or xo == 'i' or \
           xo == 'N' or xo == 'n' or \
           xo == 'S' or xo == 's' or \
           xo == 'H' or xo == 'h' or \
           xo == 'R' or xo == 'r' or \
           xo == 'D' or xo == 'd' or \
           xo == 'L' or xo == 'l' or \
           xo == 'U' or xo == 'u' or \
           xo == ' ':
           score += 9
    return score

def to_string(s):
    res = [chr(x) for x in s]
    return ''.join(res)

def hexdigit_to_dec(h):
    if '0' <= h and h <= '9':
        return ord(h) - ord('0')
    elif 'a' <= h and h <= 'f':
        return ord(h) - ord('a') + 10
    elif 'A' <= h and h <= 'F':
        return ord(h) - ord('A') + 10