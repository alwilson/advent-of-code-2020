#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

for i in items:
    print(i)

count = 0

for i in items:
    range = i[0].split('-')
    min = int(range[0])
    max = int(range[1])
    letter = i[1][0]
    pw = i[2]

    pattern = f'\\b([^{letter}]*{letter}[^{letter}]*){{{min},{max}}}\\b'

    matches = re.search(pattern, pw)

    print(min, '-', max,'-', letter, '-', pw, '-', pattern, matches)
    if matches:
        #second_try = pw.count(letter)
        #if max < second_try or second_try < min:
        #    print("we goofed!")
        #    exit()
        count += 1

print(count)

