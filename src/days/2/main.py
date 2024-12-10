#!/usr/bin/env python3

with open('example_input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

input = []
for line in data:
    input.append((line.split(' ')))

for line in input:
    safe = False
    prev_digit = int(line[0])
    prev_diff = 0
    for i in range(1,(len(line))):
        difference = int(line[i]) - prev_digit
        if difference * prev_diff < 0:
            safe = False
            break
        if 0 < abs(difference) < 4:
            safe = True
        else:
            safe = False
            break
        prev_digit = int(line[i])
        prev_diff = difference
    if safe:
        answer1 += 1

print(answer1)

for line in input:
    safe = 0
    prev_digit = int(line[0])
    prev_diff = 0
    for i in range(1,(len(line))):
        difference = int(line[i]) - prev_digit
        if difference * prev_diff < 0:
            safe = False
            break
        if 0 < abs(difference) < 4:
            safe += 0
        else:
            safe += 1
            break
        prev_digit = int(line[i])
        prev_diff = difference
    if safe > 1:
        answer1 += 1

print(answer1)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
