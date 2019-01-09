#!/usr/bin/env python3
# cryptopals set 1 challenge 8

import cpals


with open('./08.txt') as f:
    lines = [line.rstrip() for line in f]
f.close()

maxline = 0
maxscore = 0
for line in lines:
    score = cpals.detect_cbc(line)
    if score > maxscore:
        maxscore = score
        maxline = line

print('{} matches on line {}'.format(maxscore, maxline))
