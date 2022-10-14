from turtle import Turtle

SPEED = 50
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor()+SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-SPEED
        self.goto(self.xcor(), new_y)