#!/usr/bin/env python
# Cryptopals utility functions

from itertools import zip_longest, cycle

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def hexs_to_bstr(s):
    sr = ""
    for i in range(0,len(s),2):
        hexs = s[i:i+2]
        sr += chr(int(hexs,16))
    return sr

def hexs_to_intl(s):
    res = []
    for i in range(0,len(s),2):
        hexs = s[i:i+2]
        res.append(int(hexs,16))
    return res

def hexs_to_list(s):
    res = []
    for x in s:
        num = hexdigit_to_dec(x)
        res.append(num)
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

def xor(s, v):
    res = [x^v for x in s]
    return res

def xor_loop(s):
    maxscore = 0
    maxbyte = 0
    for i in range(256):
        m = xor(s,i)
        score = score_string(m)
        if score > maxscore:
            maxscore = score
            maxbyte = i
    return (maxscore,maxbyte)

def xor_repeatkey(m,k):
    res = []
    for a,b in zip(m,cycle(k)):
        res.append(a^b)
    return res

def score_string(s):
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

def to_bytes(s):
    res = [ord(x) for x in s]
    return res

def to_hexstring(s):
    res = ''
    for x in s:
        res += str("{0:02x}".format(x))
    return res

def hexdigit_to_dec(h):
    if '0' <= h and h <= '9':
        return ord(h) - ord('0')
    elif 'a' <= h and h <= 'f':
        return ord(h) - ord('a') + 10
    elif 'A' <= h and h <= 'F':
        return ord(h) - ord('A') + 10
    else:
        return 0

def calc_editdist(s1, s2):
    ed = 0
    for a,b in zip(s1,s2):
        x = a^b
        ed += bin(x).count("1")
    return ed
