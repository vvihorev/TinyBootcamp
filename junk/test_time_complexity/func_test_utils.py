import time
from random import randint


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f'The function `{func.__name__}` took\t{time.time() - start:.7f} seconds')
    return wrapper


def generate_input(n):
    with open(f'input-{n}.txt', 'w') as file:
        for _ in range(n):
            file.write(f'{randint(1, 10000)}\n')


def read_list_of_integers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        nums = [int(line.strip()) for line in lines]
    return nums

