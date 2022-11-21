from random import randint


secret = randint(100, 999)
first = secret // 100
second = secret // 10 % 10
third = secret % 10

for i in range(5):
    a = int(input())
    b = int(input())
    c = int(input())

    if first == a:
        print("First right")
    elif second == a or third == a:
        print("First in wrong place")
    else:
        print("First wrong")

    if second == b:
        print("Second right")
    elif first == b or third == b:
        print("Second in wrong place")
    else:
        print("Second wrong")

    if third == c:
        print("Third right")
    elif first == c or second == c:
        print("Third in wrong place")
    else:
        print("Third wrong")
