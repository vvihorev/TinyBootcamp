import matplotlib.pyplot as plt


def get_derivative(func, x, delta=0.1):
    return round((func(x + delta) - func(x - delta)) / (2 * delta), 2)


def parabola(x):
    return x**2 


def polynome(x):
    return x**3 - 20*x**2 + 40*x - 100


def newton_method(func, x, epsilon=0.001):
    step = 0
    while abs(func(x)) > epsilon:
        print(f"{step}: {x}\t{func(x)}")
        step += 1
        x = x - func(x)/get_derivative(func, x)
    return x


def print_derivative_table(func):
    print("x\tsquare\tderivative")
    print("--------------------------")
    for x in range(-10, 11):
        print(f"{x}\t{func(x)}\t{get_derivative(func, x)}")


def find_zeroes():
    func = parabola
    x = [x for x in range(-20, 30)]
    y = [func(x_i) for x_i in x]

    plt.plot(x, y)
    plt.grid()
    plt.show()

    res = newton_method(func, -10)

find_zeroes()
