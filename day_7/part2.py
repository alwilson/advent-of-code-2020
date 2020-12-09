#!/usr/bin/env python3

with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

contains = {}

for i in items:
    contain_split = i.split(' bags contain')
    outside_bag = contain_split[0]
    inside_bags = contain_split[1][:-1]
    for ibag in inside_bags.split(','):
        bags = ibag.split(' ')
        num_bags = bags[1]
        bag_color = ' '.join(bags[2:4])
        if bag_color == 'other bags':
            continue
            #contains[outside_bag] = []
        if outside_bag not in contains:
            contains[outside_bag] = [(bag_color, int(num_bags))]
        else:
            contains[outside_bag].append((bag_color, int(num_bags)))

queue = []
queue = contains['shiny gold']
visited = ['shiny gold']
bag_count = 0

while len(queue):
    current_bag, num_bags = queue.pop()
    print(f'{current_bag}: bag_count: {bag_count} queue: {queue}')
    #assert current_bag not in visited
    visited.append(current_bag)
    bag_count += int(num_bags)
    if current_bag not in contains:
        continue
    for b in contains[current_bag]:
        queue.append((b[0], b[1] * num_bags))

print(bag_count)
