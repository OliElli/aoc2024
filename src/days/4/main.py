#!/usr/bin/env python3

with open('src/days/4/input.txt') as f:
    data = f.read().splitlines()

answer1 = 0
answer2 = 0

def create_directions():
    directions = []
    for x in range(-1,2):
        for y in range(-1,2):
            if x == 0 and y == 0:
                continue
            directions.append((x, y))
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

tx = len(data)      # number of rows
ty = len(data[0])   # number of columns

def has_x_mas(i, j):
    # Stay inside the grid + 1 border character
    if not (1 <= i < tx - 1 and 1<= j < ty - 1):
        return False
    if data[i][j] != 'A':
        return False

    # Check diagonals
    diag1 = data[i-1][j-1] + data[i+1][j+1]
    diag2 = data[i-1][j+1] + data[i+1][j-1]

    if diag1 in ['MS','SM'] and diag2 in ['MS','SM']:
        return True
    return False

for i in range(tx):
    for j in range(ty):
        if has_x_mas(i, j):
            answer2 += 1

print(answer1)
print(answer2)

with open('src/days/4/answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
