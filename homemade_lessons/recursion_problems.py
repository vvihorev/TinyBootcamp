
def palyndrome(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palyndrome(s, l+1, r-1)


def test_palyndrome():
    assert palyndrome("abccba", 0, 5)
    assert palyndrome("abcba", 0, 4)
    assert palyndrome("abcbad", 0, 5)
    assert palyndrome("abcaba", 0, 5)


def print_odd():
    n = int(input())
    if n % 2 == 1:
        print(n)
    print_odd()


def return_max(max):
    n = int(input())
    if n == 0:
        return max
    if n > max:
        max = n
    return return_max(max)


print(return_max(0))
