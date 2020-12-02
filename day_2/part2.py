#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [x.strip().split(' ') for x in fd]

count = 0

for i in items:
    range = i[0].split('-')
    min = int(range[0])
    max = int(range[1])
    letter = i[1][0]
    pw = i[2]

    if (pw[min-1] == letter) ^ (pw[max-1] == letter):
        count += 1

print(count)

