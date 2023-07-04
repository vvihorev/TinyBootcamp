import math
import turtle


wn = turtle.Screen()
wn.setup(600, 600)
wn.tracer(0)

WIDTH = wn.window_width()
HEIGHT = wn.window_height()

BALLS = []


class Ball:
    def __init__(self, x, y, vx=10, vy=5) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def update(self):
        if abs(self.x) > 200:
            self.vx *= -1
        if abs(self.y) > 200:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        self.t.clear()
        circle(self.t, self.x, self.y, radius=2)


class Base:
    def __init__(self) -> None:
        self.x = 0
        self.y = -200
        self.vx = 0

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

    def update(self):
        pass

    def draw(self):
        rectangle(self.t, self.x, self.y, 80, 5)


def spawn_ball(x, y):
    BALLS.append(Ball(x, y))


def circle(t, x, y, radius=5, polygons=20, fillcolor="black", pencolor="black"):
    phi = 360 // polygons
    t.penup()
    t.goto(x, y)
    t.forward(radius)
    t.left(90 + phi//2)
    t.pendown()

    t.fillcolor(fillcolor)
    t.pencolor(pencolor)
    t.begin_fill()

    for _ in range(polygons):
        t.forward(2*radius*math.cos(phi))
        t.left(phi)
    t.right(90 + phi//2)

    t.end_fill()


def rectangle(t, x, y, width, height):
    t.penup()
    t.goto(x - width//2, y - height//2)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


base = Base()

while True:
    base.draw()
    for ball in BALLS:
        ball.update()
        ball.draw()
    wn.update()

    wn.onclick(spawn_ball)

# wn.mainloop() 

