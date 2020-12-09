#!/usr/bin/env python3

import string

with open('./input.txt') as fd:
    # items = [x.strip().split(' ') for x in fd]
    items = fd.read()
    items = items.split('\n\n')

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
count = 0
year_checks = {'byr': [1920, 2002], 'iyr': [2010, 2020], 'eyr': [2020, 2030]}
hgt_check = {'cm': [150, 193], 'in': [59, 76]}
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for i in items:
    infos = i.split()
    labels = set()
    for info in infos:
        v :str
        (l, v) = info.split(':')
        print(l, v)
        valid = False
        if l in year_checks.keys():
            if len(v) == 4 and v.isnumeric() and year_checks[l][0] <= int(v) <= year_checks[l][1]:
                valid = True
        elif l == 'hgt':
            if v.endswith('cm') or v.endswith('in'):
                v1 :str = v[:-2]
                v2 :str = v[-2:]
                if v1.isnumeric() and hgt_check[v2][0] <= int(v1) <= hgt_check[v2][1]:
                    valid = True
        elif l == 'hcl':
            if v[0] == '#' and len(v) == 7 and all(c in string.hexdigits for c in v[1:]):
                valid = True
        elif l == 'ecl':
            if v in valid_eye_colors:
                valid = True
        elif l == 'pid':
            if v.isnumeric() and len(v) == 9:
                valid = True
        elif l == 'cid':
            valid = True

        if valid:
            labels.add(l)

    print(labels)
    if len(labels.intersection(required)) == len(required):
        count += 1

print(count)

