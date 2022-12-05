"""
Примеры решения задач по модулю turtle от МФТИ.
Можно подсмотреть идеи решений, если попадешь в ступор
"""

import math
import time
import turtle as t
t.speed(0)


def square_spiral():
    step = 10
    for i in range(20):
        t.forward(step)
        t.left(90)
        t.forward(step)
        t.left(90)
        step += 10
    time.sleep(3)


def inner_squares():
    start = 10
    for _ in range(10):
        step = start * 2
        t.penup()
        t.goto(-start, -start)
        t.pendown()
        for _ in range(4):
            t.forward(step)
            t.left(90)
        start += 10
    time.sleep(3)


def draw_circle(r, polygons=30):
    phi = 360 / polygons
    t.left(phi / 2)
    for _ in range(polygons):
        t.forward(2 * r * abs(math.sin(phi / 2)))
        t.left(phi)
    t.right(phi / 2)


def draw_square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)

for r in range(50, 5, -5):
    draw_circle(r)

# start = 10
# for _ in range(10):
    # t.penup()
    # t.goto(-start, -start)
    # t.pendown()
    # draw_square(start*2)
    # start += 10
# time.sleep(1)
