#!/usr/bin/env python3

with open('input.txt') as f:
    data = f.read().splitlines()

list1 = []
list2 = []
for line in data:
    values = line.split('   ')
    list1.append(int(values[0]))
    list2.append(int(values[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

total1 = 0
for i in range(len(list1)):
    if sorted_list1[i] >= sorted_list2[i]:
        total1 += sorted_list1[i] - sorted_list2[i]
    else:
        total1 += sorted_list2[i] - sorted_list1[i]

print(f"Pt1: {total1}")

total2 = 0
for i in range(len(list1)):
    matched_value = [j for j in list2 if j == list1[i]]
    total2 += len(matched_value) * list1[i]

print(f"Pt2: {total2}")

with open('answers.txt', 'w') as f:
    f.write(f"{total1}\n")
    f.write(f"{total2}\n")
