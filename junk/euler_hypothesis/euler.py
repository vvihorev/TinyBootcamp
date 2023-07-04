import time



def euler():
    for a in range(133, 134):
        for b in range(110, a+1):
            for c in range(84, b+1):
                for d in range(27, c+1):
                    x = (a**5 + b**5 + c**5 + d**5) ** (1/5)
                    print(a, b, c, d)
                    if int(x) == x:
                        return a, b, c, d

start = time.time()
res = euler()
print(res)
print(f"took {time.time() - start} seconds")

