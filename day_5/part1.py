#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

vals = []
for i in items:
    row = ''
    for r in i[:7]:
        if r == 'B':
            row += '1'
        else:
            row += '0'

    col = ''
    for c in i[7:]:
        if c == 'R':
            col += '1'
        else:
            col += '0'

    vals += [int(row + col, 2)]

print(vals)
print(max(vals))