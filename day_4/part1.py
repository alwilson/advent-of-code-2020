#!/usr/bin/env python3

with open('./input.txt') as fd:
    #items = [x.strip().split(' ') for x in fd]
    items = fd.read()
    items = items.split('\n\n')

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
count = 0
for i in items:
    infos = i.split()
    labels = set()
    for info in infos:
        labels.add(info.split(':')[0])

    print(labels)
    if len(labels.intersection(required)) == len(required):
        count += 1

print(count)

