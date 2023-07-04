# Принцип разделяй и властвуй
# Чтобы решить задачу можно найти самый простой возможный случай, и упрощать проблему, пока мы до него не дойдем


# 1. Найти максимально возможную длину стороны квадратного участка землки, в которых можно без остатка отсчитывать участки земли на площади x*y метров

def find_max_square_side(x, y):
    if x % y == 0:
        return y
    return find_max_square_side(y, x % y)


print(find_max_square_side(165, 120))


# 2. Найти сумму списка чисел, не используя циклов

def my_sum(lst):
    if lst == []:
        return 0
    return lst[0] + my_sum(lst[1:])


print(my_sum([1, 2, 3]))


# 2.1 Найти максимум списка рекурсивно
def my_max(lst, max):
    if lst == []:
        return max
    if lst[0] > max:
        return my_max(lst[1:], lst[0])
    return my_max(lst[1:], max)


print(my_max([1, 4, 3, 2, 5, 4, 7], 1))

# 3. Осортировать список 

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = []
    more = []
    for element in lst[1:]:
        if element < pivot:
            less.append(element)
        else:
            more.append(element)
    return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([3, 1, 5, 4, 7, 5, 9, 0, 2, 4, 1, 5, 4, 8, 10]))


import time
from random import randint

list_100 = [randint(1, 10000) for _ in range(1000)]
list_1000 = [randint(1, 10000) for _ in range(10000)]
list_10000 = [randint(1, 10000) for _ in range(100000)]


for lst in list_100, list_1000, list_10000:
    start = time.time()
    quicksort(lst)
    print(f"Took {time.time() - start} seconds")
