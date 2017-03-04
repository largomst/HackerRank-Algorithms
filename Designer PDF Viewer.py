#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
word_height_list = list()
for alpha in word:
    word_height_list.append(h[ord(alpha) - ord('a')])
squera = max(word_height_list) * len(word)
print(squera)
