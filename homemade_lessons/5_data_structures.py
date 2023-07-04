def swap_two(a, b):
    c = a
    a = b
    b = c
    return a, b


a = [5, 2, 4, 6, 1, 3, 8, 9, 0, 10]
"""
# Для каждого индекса i в диапазоне от нуля до длины списка a, напечатать i-тый элемент a
for i in range(len(a)): 
    print(a[i])

# Для каждого элемента в списке a напечатать элемент
for elem in a:
    print(elem)

# Что делает этот цикл?
for i in range(len(a)):
    if 3 <= i <= 6:
        print(a[i])

# А этот?
for elem in a:
    if 3 <= elem <= 6:
        print(elem)
    else:
        print()

# Срезы списка
print(a)
print(a[-3:])
# print(a[len(a) - 1:0:-1])

"""

def insert_sort(a):
    count = 0
    for j in range(1, len(a)):
        for i in range(1, len(a)):
            count += 1
            if a[i - 1] < a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
    print(count)
    return a


b = insert_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(b[::-1])
# print(insert_sort(a))
"""

def find_max(a):
    return max_elem


def find_two_max(a):
    return first_max, second_max


def find_max_and_min(a):
    return min_elem, max_elem


def has_two_sum(nums, target):
    # TODO: функция возвращает True если в массиве есть два элемента, дающие в сумме target
    return has_two_sum
def has_two_sum(nums, target):
    # TODO: функция возвращает индексы пары элементов
    return has_two_sum
def has_two_sum(nums, target):
    # TODO: функция возвращает все возможные пары элементов
    return has_two_sum


def find_unique_letters(seq):
    return unique


def count_letters(seq):
    return letter_count


seq = "Hello, world! How are you all doing today?"
count = count_letters(seq)

# TODO: добавить код из примеров в текст урока
"""
