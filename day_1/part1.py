#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [int(x.strip()) for x in fd]

items.sort()
# print(items)

itemd = {}
for i in items:
    itemd[i] = True

for i in items:
    target = 2020 - i
    if target in itemd:
        print(target, i, target * i)
        break
