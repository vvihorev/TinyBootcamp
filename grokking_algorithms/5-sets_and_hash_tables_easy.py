from random import randint
import time
# Давай напишем хэш функцию для чисел

def hash_number(x):
    return x % 255

# Давай соберем собственную хэш-таблицу
# Давай обработаем коллизии в хэше

def insert(hash_table, key, value):
    values = hash_table[hash_number(key)]
    for k, _ in values:
        if k == key:
            return
    values.append((key, value))


def get(hash_table, key):
    values = hash_table[hash_number(key)]
    for k, v in values:
        if k == key:
            return v
    return None


def remove(hash_table, key):
    values = hash_table[hash_number(key)]
    for k, v in values:
        if k == key:
            values.remove((k, v))
            return


def create_hash_table():
    hash_table = []
    for _ in range(255):
        hash_table.append([])
    return hash_table


# my_first_hash_table = create_hash_table()
# insert(my_first_hash_table, 2, 'papa')
# insert(my_first_hash_table, 12345, 'son')
# insert(my_first_hash_table, 678, 234)
# insert(my_first_hash_table, 104, 234)
# print(get(my_first_hash_table, 2))
# print(get(my_first_hash_table, 12345))
# print(get(my_first_hash_table, 678))
# print(get(my_first_hash_table, 104))



# Для чего хороши хэш-таблицы?
# 1. Отношения ключ-значение
# 2. Устранение дубликатов
# 3. Кэширование, запоминание данных


# Упражнение: отбираем уникальные элементы с помощью хэш-таблицы и без

# [1, 3, 2, 2, 1, 5, 6, 7, 5, 5, 3, 2]
# [1, 3, 2, 5, 6, 7]


def get_unique_elements_slow(lst):
    unique = []
    for element in lst:
        already_seen = False

        for seen_element in unique:
            if element == seen_element:
                already_seen = True

        if not already_seen:
            unique.append(element)
    return unique


def get_unique_elements(lst):
    already_seen = create_hash_table()
    unique = []
    for element in lst:
        seen = get(already_seen, element)
        if seen is None:
            unique.append(element)
            insert(already_seen, element, 1)
    return unique


def get_unique_elements_pythonic(lst):
    already_seen = set()
    unique = []
    for element in lst:
        if element not in already_seen:
            already_seen.add(element)
            unique.append(element)
    return unique


print("Проверяем скорость работы функции поиска уникальных чисел в списке из 10000 элементов")
print("-----")
lst = [randint(0, 100000) for _ in range(10000)]

start = time.time()
get_unique_elements_slow(lst)
print(f"Каждый раз проверять по списку, встречался ли уже элемент: {time.time() - start:.4f} секунд")

start = time.time()
get_unique_elements(lst)
print(f"Наша самодельная хэш таблица: {time.time() - start:.4f} секунд")

start = time.time()
get_unique_elements_pythonic(lst)
print(f"Хэш таблица питона: {time.time() - start:.4f} секунд")
print()


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_cached(n, cache):
    value = get(cache, n)
    if value is None:
        insert(cache, n, fibonacci(n-1) + fibonacci(n-2))
    return get(cache, n)


print("Проверяем скорость работы функции поиска уникальных чисел в списке из 10000 элементов")
print("-----")
lst = [randint(0, 100000) for _ in range(10000)]

start = time.time()
get_unique_elements_slow(lst)
print(f"Каждый раз проверять по списку, встречался ли уже элемент: {time.time() - start:.4f} секунд")

start = time.time()
get_unique_elements(lst)
print(f"Наша самодельная хэш таблица: {time.time() - start:.4f} секунд")

start = time.time()
get_unique_elements_pythonic(lst)
print(f"Хэш таблица питона: {time.time() - start:.4f} секунд")
print()

def hash_number(x):
    pass

def insert(hash_table, key, value):
    pass


def get(hash_table, key):
    pass


def remove(hash_table, key):
    pass


def create_hash_table():
    pass

def hash_number(x):
    return x % 255

# Давай соберем собственную хэш-таблицу
# Давай обработаем коллизии в хэше

def insert(hash_table, key, value):
    values = hash_table[hash_number(key)]
    for k, _ in values:
        if k == key:
            return
    values.append((key, value))


def get(hash_table, key):
    values = hash_table[hash_number(key)]
    for k, v in values:
        if k == key:
            return v
    return None


def remove(hash_table, key):
    values = hash_table[hash_number(key)]
    for k, v in values:
        if k == key:
            values.remove((k, v))
            return


def create_hash_table():
    hash_table = []
    for _ in range(255):
        hash_table.append([])
    return hash_table
