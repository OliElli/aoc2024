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

wrong_order = []
for pages in page_numbers:
    if eval_order(pages):
        answer1 += find_middle_value(pages)
    else:
        wrong_order.append(pages)

def fix_order(pages, result = None):
    for order in page_orders:
        if order[0] in pages and order[1] in pages:
            a = pages.index(order[0])
            b = pages.index(order[1])
            if a > b:
                pages[a], pages[b] = pages[b], pages[a]
    if eval_order(pages):
        result = find_middle_value(pages)
        return result
    else:
        result = fix_order(pages)
        return result


# Pt2
# Fix the ordering
for pages in wrong_order:
    answer2 += fix_order(pages)

print(answer1)
print(answer2)

with open('src/days/5/answers.txt', 'w') as f:
    f.write(f"{answer1}\n")
    f.write(f"{answer2}\n")
