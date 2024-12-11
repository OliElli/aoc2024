#!/usr/bin/env python3

import re

with open('example_input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

# pt1
for line in data:
    ops = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
    for op in ops:
        print(op)
        a, b = map(int, re.findall(r'[0-9]+', op))
        print(a, b)
        answer1 += a * b

print(answer1)
print(answer2)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
