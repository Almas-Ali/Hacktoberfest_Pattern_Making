from turtle import Turtle


FONT = ('Courier', 80, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(2, 200)
        self.content()

    def content(self):
        self.write(f"{self.l_score}  {self.r_score}", False, align="center", font=FONT)

    def l_update(self):
        self.clear()
        self.l_score += 1
        self.content()

    def r_update(self):
        self.clear()
        self.r_score += 1
        self.content()


