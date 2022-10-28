import time
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
from time import sleep

game_screen = Screen()
game_screen.setup(width=800, height=600)
game_screen.bgcolor("black")
game_screen.title("Pong Game")
game_screen.tracer(0)

score = ScoreBoard()


dash_line_up = Turtle()
dash_line_up.color("white")
dash_line_up.penup()
dash_line_up.goto(0, 300)
while dash_line_up.ycor() > -310:
    dash_line_up.setheading(270)
    dash_line_up.forward(10)
    dash_line_up.penup()
    dash_line_up.fd(10)
    dash_line_up.pendown()


r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

game_screen.listen()
game_screen.onkey(fun=r_paddle.up, key="w")
game_screen.onkey(fun=r_paddle.down, key="s")

game_screen.onkey(fun=l_paddle.up, key="Up")
game_screen.onkey(fun=l_paddle.down, key="Down")

is_on = True
while is_on:
    game_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with upper wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with side wall
    if ball.xcor() > 380:
        ball.refresh()
        l_paddle.score = score.l_update()
    elif ball.xcor() < -380:
        ball.refresh()
        r_paddle.score = score.r_update()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()










game_screen.exitonclick()