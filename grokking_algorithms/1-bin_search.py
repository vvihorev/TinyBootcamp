import time
from random import randint

list_100 = sorted([randint(1, 10000) for _ in range(1000)])
list_1000 = sorted([randint(1, 10000) for _ in range(10000)])
list_10000 = sorted([randint(1, 10000) for _ in range(100000)])


def bin_search(lst, item):
    if lst == []:
        return -1
    mid = len(lst) // 2
    if item == lst[mid]:
        return mid
    if item > lst[mid]:
        return bin_search(lst[mid+1:], item)
    return bin_search(lst[:mid], item)
    

for lst in list_100, list_1000, list_10000:
    item = lst[randint(0, len(lst)-1)]
    start = time.time()
    bin_search(lst, item)
    print(f"Took {time.time() - start} seconds")
