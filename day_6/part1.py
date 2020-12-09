#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = fd.read()
    items = items.split('\n\n')

print(items)
count = 0
for grp in items:
    answers = set([c for g in grp.split() for c in g])
    print(grp.split(), answers)
    count += len(answers)

print(count)
