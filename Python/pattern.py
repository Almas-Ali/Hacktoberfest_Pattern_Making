#simple pattern using turtle python library Made by Hitch Hicker
import turtle
t = turtle.Turtle()
sc=turtle.Screen()
sc.title("Hitch Hicker")
sc.bgcolor("black")
t.hideturtle()
list = ["purple","green","blue","red","orange"]
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)