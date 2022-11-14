def even(n):
    return n % 2 == 0


def test_even():
    assert even(5) == False
    assert even(4) == True
