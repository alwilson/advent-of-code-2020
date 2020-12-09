#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

count = 0
trees = 0
for i in items:
    if i[count % len(i)] == '#':
        trees += 1
    count += 3

print(trees)

