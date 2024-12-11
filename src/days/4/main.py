#!/usr/bin/env python3

import re

with open('input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

def create_directions():
    directions = []
    for x2 in range(-1,2):
        for y2 in range(-1,2):
            if x2 == 0 and y2 == 0:
                continue
            directions.append((x2, y2))
    return(directions)

def get_char(data, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return data[y][x]
    except IndexError:
        return None

def find_mas(data, x, y, direction, char_num=1):
    if char_num == 4:
        return True
    next_char = get_char(data, x+direction[0], y+direction[1])
    if next_char == 'XMAS'[char_num]:
        result = find_mas(data, x+direction[0], y+direction[1], direction, char_num+1)
        if result:
            return True
    return False

def find_as(data, x, y, direction, char_num=1):
    if char_num == 3:
        return True
    next_char = get_char(data, x+direction[0], y+direction[1])
    if next_char == 'MAS'[char_num]:
        result = find_as(data, x+direction[0], y+direction[1], direction, char_num+1)
        if result:
            return True
    return False

# pt1
directions = create_directions()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == 'X':
            # Find MAS
            for direction in directions:
                answer = find_mas(data, x, y, direction)
                if answer:
                    answer1 += 1

# pt2
# 1 find diagonal MAS
# cross MAS can be x1=x2, direction = crossed
#                  y1=y2, direction = crossed
# directions2 = [(1,1), (1,-1), (-1,-1), (-1,1)]
# mases = []
# for y, line in enumerate(data):
#     for x, char in enumerate(line):
#         if char == 'M':
#             # Find AS
#             for direction in directions2:
#                 answer = find_as(data, x, y, direction)
#                 if answer:
#                     mases.append(((x,y), direction))
#                     # Find a crossed MAS
#                     pass
# for coords, direction in mases:
#     print(coords, direction)
#     starter_coords = ((coords[0] + direction[0] * 2, coords[1]),(coords[0], coords[1] + direction[0] * 2))
#     print(starter_coords)
#     print()

print(answer1)
print(answer2)

with open('answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
