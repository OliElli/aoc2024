#!/usr/bin/env python3

import re

with open('input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

input = "".join(data)

# pt1
ops = re.findall(r'mul\([0-9]+,[0-9]+\)', input)
for op in ops:
    a, b = map(int, re.findall(r'[0-9]+', op))
    answer1 += a * b

#pt2
donts = re.split(r'don\'t', input)
print(donts)

print(answer1)
print(answer2)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
