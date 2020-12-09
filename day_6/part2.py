#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = fd.read()
    items = items.split('\n\n')

print(items)
count = 0
for grp in items:
    answers = set()
    for idx, g in enumerate(grp.split('\n')):
        answer = set([c for c in g])
        if idx == 0:
            answers = answer
        else:
            answers = answers.intersection(answer)

    print(grp.split(), answers)
    count += len(answers)

print(count)
