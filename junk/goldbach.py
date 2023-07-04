def test_goldbach(n):
    for i in range(1, n): 
        if is_prime(i) and is_prime(n - i):
            print(f"for {n}: {i, n-i}")
            return True
    return False
        


def is_prime(n):
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            return False
    return True



for i in range(2, 81, 2):
    test_goldbach(i)

