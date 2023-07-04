def countdown(n):
    print(n)
    if n == 0:
        return
    countdown(n-1)


def recurse_sum(lst):
    if lst == []:
        return 0
    return lst[0] + recurse_sum(lst[1:])

print(recurse_sum([1, 2, 3, 4, 5]))