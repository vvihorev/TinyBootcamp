from random import randint
import time
import turtle as t


def square(step, unit=t):
    for _ in range(4):
        unit.forward(step)
        unit.left(90)


def square_flower(leaves, unit=t):
    for _ in range(leaves):
        square(20, unit)
        unit.left(360 / leaves)


def flower_table():
    leaves = 1
    for i in range(60, -61, -60):
        for j in range(-280, 281, 60):
            now = t.Turtle(shape="classic")
            now.ht()
            now.speed(0)
            now.penup()
            now.goto(j, i)
            now.pendown()
            square_flower(leaves, now)
            leaves += 1


def model_gas():
    unit_count = 10
    pool = []
    for i in range(unit_count):
        this = t.Turtle(shape='circle')
        this.speed(0)
        this.penup()
        this.goto(randint(-200, 200), randint(-200, 200))
        pool.append(this)

    for _ in range(200):
        for unit in pool:
            unit.forward(2)


def model_point():
    point = t.Turtle()
    point.shape('circle')

    x, y = -200, 0 
    point.goto(x, y)
    vx, vy = 10, 30
    ay = -9.8

    dt = 0.2
    while True:
        dx = vx*dt
        dy = vy*dt + ay*dt**2/2
        vy += ay*dt
        if y + dy < 0:
            vy = -vy * 0.8
        x += dx
        y += dy
        point.goto(x, y)
    

model_point()
time.sleep(2)

