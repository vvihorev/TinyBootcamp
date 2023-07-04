def max_den_sum(a, b):
    best = 0
    best_sum = 0
    for x in range(a, b+1):
        sum = 0
        for i in range(1, x+1):
            if x % i == 0:
                sum += i
        if sum > best_sum:
            best = x
            best_sum = sum
    return best, best_sum


print(max_den_sum(1, 100))

