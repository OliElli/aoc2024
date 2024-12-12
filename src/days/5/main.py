#!/usr/bin/env python3

with open('src/days/5/input.txt') as f:
    data = f.read()

answer1 = 0
answer2 = 0

page_orders,page_numbers = data.split('\n\n')
page_orders = [[int(j) for j in i.split('|')] for i in page_orders.split('\n')]
page_numbers = [[int(k) for k in j] for j in [i for i in [i.split(',') for i in page_numbers.split('\n')[:-1]]]]

def eval_order(pages):
    for order in page_orders:
        if order[0] in pages and order[1] in pages:
            if pages.index(order[0]) > pages.index(order[1]):
                return False
    return True

def find_middle_value(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        print('no middle value', lst)
        return lst[n // 2 - 1]

for pages in page_numbers:
    if eval_order(pages):
        answer1 += find_middle_value(pages)

print(answer1)
print(answer2)

with open('src/days/5/answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
