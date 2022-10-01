import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(1)
t.pensize(2)
t.pencolor("white")


def s_curve():
    for i in range(90):
        t.left(1)
        t.forward(1)


def r_curve():
    for i in range(90):
        t.right(1)
        t.forward(1)


def l_curve():
    s_curve()
    t.forward(80)
    s_curve()


def l_curve1():
    s_curve()
    t.forward(90)
    s_curve()


def half():
    t.forward(50)
    s_curve()
    t.forward(90)
    l_curve()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(120)  # on test
    l_curve1()
    t.forward(30)
    t.left(90)
    t.forward(50)
    r_curve()
    t.forward(40)
    t.end_fill()


def get_pos():
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.pendown()


def eye():
    t.penup()
    t.right(90)
    t.forward(160)
    t.left(90)
    t.forward(70)
    t.pencolor("black")
    t.dot(35)


def sec_dot():
    t.left(90)
    t.penup()
    t.forward(310)
    t.left(90)
    t.forward(120)
    t.pendown()

    t.dot(35)


t.fillcolor("#306998")
t.begin_fill()
half()
t.end_fill()
get_pos()
t.fillcolor("#FFD43B")
t.begin_fill()
half()
t.end_fill()

eye()
sec_dot()


def pause():
    t.speed(2)
    for i in range(100):
        t.left(90)


pause()
