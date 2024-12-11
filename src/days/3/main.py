#!/usr/bin/env python3

import re

with open('example_input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

print(data)
print(re.split(r'', data))

print(answer1)
print(answer2)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
