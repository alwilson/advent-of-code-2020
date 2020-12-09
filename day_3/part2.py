#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

count = 0
trees = 0
tree_vals = 1
for i in items:
    if i[count % len(i)] == '#':
        trees += 1
    count += 1

print(trees)
tree_vals *= trees

count = 0
trees = 0
for i in items:
    if i[count % len(i)] == '#':
        trees += 1
    count += 3

print(trees)
tree_vals *= trees

count = 0
trees = 0
for i in items:
    if i[count % len(i)] == '#':
        trees += 1
    count += 5

print(trees)
tree_vals *= trees

count = 0
trees = 0
for i in items:
    if i[count % len(i)] == '#':
        trees += 1
    count += 7

print(trees)
tree_vals *= trees

count = 0
trees = 0
for item_idx, i in enumerate(items):
    if item_idx % 2 == 0:
        if i[count % len(i)] == '#':
            trees += 1
        count += 1

print(trees)
tree_vals *= trees

print(f'tree_vals: {tree_vals}')