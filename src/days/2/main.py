#!/usr/bin/env python3

from itertools import pairwise

with open('input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

input = [[int(i) for i in line.split()] for line in data]

def test(input):
    prev_diff = 0
    for previous, current in pairwise(input):
        if not 0 < abs(previous - current) < 4:
            return False
        difference = current - previous
        if difference * prev_diff < 0:
            return False
        if previous == current:
            return False
        prev_diff = difference
    return True

for report in input:
    if test(report):
        answer1 += 1
    else:
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            if test(report_copy):
                answer2 += 1
                break
answer2 += answer1

print(answer1)
print(answer2)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
