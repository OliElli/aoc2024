#!/usr/bin/env python3

with open('input.txt') as f:
    data = f.read().splitlines()

list1 = []
list2 = []
for line in data:
    values = line.split('   ')
    list1.append(int(values[0]))
    list2.append(int(values[1]))

list1 = sorted(list1)
list2 = sorted(list2)

total = 0
for i in range(len(list1)):
    if list1[i] >= list2[i]:
        total += list1[i] - list2[i]
    else:
        total += list2[i] - list1[i]

print(total)
