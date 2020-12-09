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
        if bag_color not in contains:
            contains[bag_color] = [(outside_bag, num_bags)]
        else:
            contains[bag_color].append((outside_bag, num_bags))

queue = []
queue = contains['shiny gold']
visited = ['shiny gold']
color_count = 0

while len(queue):
    current_bag = queue.pop()[0]
    print(f'{current_bag}: color_count: {color_count} queue: {queue}')
    if current_bag in visited:
        continue
    visited.append(current_bag)
    color_count += 1
    if current_bag not in contains:
        continue
    for b in contains[current_bag]:
        queue.append(b)

print(color_count)

