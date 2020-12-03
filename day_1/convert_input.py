#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [int(x.strip()) for x in fd]

count = 256
with open('./input_hex.mem', 'w') as fd:
    for i in items:
        fd.write(f'{i:04x}\n')
        count -= 1

    while count > 0:
        count -= 1
        fd.write(f'0000\n')
