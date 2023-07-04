# Давай напишем хэш функцию для строк текста

def hash_string(s):
    global mod, primes
    sum = 0
    for c in s:
        number = ord(c) - ord('0')
        prime = primes[number]
        sum += prime
    return sum % mod


# Давай соберем собственную хэш-таблицу

def prepare_primes(holder, count):
    cur = 1
    while count >= 0:
        is_prime = True
        for i in range(2, int(cur**(1/2)+1)):
            if cur % i == 0:
                is_prime = False
                break
        if is_prime:
            holder.append(cur)
            count -= 1
        cur += 1


def prepare_hash_table(holder, mod):
    for _ in range(mod):
        holder.append([])


def insert(hash_table, key, value):
    values = hash_table[hash_string(key)]
    for k, _ in values:
        if k == key:
            return
    values.append((key, value))


def get(hash_table, key):
    values = hash_table[hash_string(key)]
    for k, v in values:
        if k == key:
            return v
    raise ValueError('key not found')


def remove(hash_table, key):
    values = hash_table[hash_string(key)]
    for k, v in values:
        if k == key:
            values.remove((k, v))
            return


mod = 31
primes, hash_table = [], []
prepare_primes(primes, ord('z')-ord('0'))
prepare_hash_table(hash_table, mod=mod)

insert(hash_table, 'mama', 'papa')
insert(hash_table, 'papa', 'son')
insert(hash_table, 'nanny', 234)
insert(hash_table, 'daddy', 234)
print(hash_table)
print(get(hash_table, 'papa'))
print(get(hash_table, 'mama'))
print(get(hash_table, 'nanny'))
print(get(hash_table, 'daddy'))





# Давай обработаем коллизии в хэше



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
    already_seen = set()
    unique = []
    for element in lst:
        if element not in already_seen:
            already_seen.add(element)
            unique.append(element)
    return unique


# print(get_unique_elements([1, 3, 2, 2, 1, 5, 6, 7, 5, 5, 3, 2]))

