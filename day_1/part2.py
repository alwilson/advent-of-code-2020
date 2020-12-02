#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [int(x.strip()) for x in fd]

items.sort()
#print(items)

itemd = {}
for i in items:
    itemd[i] = True

for i in items:
    for j in items:
        if i == j:
            continue
        target = 2020 - i - j
        if target in itemd:
            print(target, i, j, target * i * j)
            exit()
