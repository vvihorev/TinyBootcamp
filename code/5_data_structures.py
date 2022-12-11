a = [5, 2, 4, 6, 1, 3, 8, 9, 0, 10]


def swap_two(a, b):
    # TODO: Как поменять местами две переменных?
    return a, b


def list_printing(a):
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

    # Срезы списка
    print(a[3:6])
    print(a[::-1])


def insert_sort(a):
    for i in range(1, len(a)):
        print(a)
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


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
