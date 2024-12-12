#!/usr/bin/env python3

import re

with open('src/days/3/input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

input = "".join(data)

# pt1
def calc(input):
    answer = 0
    ops = re.findall(r'mul\([0-9]+,[0-9]+\)', input)
    for op in ops:
        a, b = map(int, re.findall(r'[0-9]+', op))
        answer += a * b
    return answer

answer1 = calc(input)

#pt2
donts = re.split(r"don't\(\)", input)
answer2 = calc(donts[0])

for i, line in enumerate(donts):
    if i == 0:
        continue
    dos = re.split(r"do\(\)", line)
    for i in range(len(dos)):
        if i > 0:
            answer2 += calc(dos[i])

print(answer1)
print(answer2)

with open('src/days/3/answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
