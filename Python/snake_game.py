# Python Program for Snake game uisng Tkinter GUI.
# Made by: Vivek Dharewa (Vice777)
# Importing the libraries

from tkinter import *
import random
from turtle import speed, window_height, window_width

window = Tk()
window.title("Snake Game")
window.resizable(0,0)

Label(window, text="Enjoy the Game", font='calibri 20').pack(side=BOTTOM)

score =0
direction = 'down'

WIDTH = 600
HEIGHT = 600
SPEED = 100
SPACE_SIZE = 40
BODY_PART =2
SNAKE_COLOR = '#7CFC00'
FOOD = '#FFFD5A'
BGCOLOR = '#000000'

label = Label(window, text= "SCORE: {}".format(score),font=('arial',40))
label.pack()

canvas = Canvas(window, bg=BGCOLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

class Snake:
    def __init__(self):
        self.body_size = BODY_PART
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PART):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates = [x,y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD, tag="food")


def next_mov(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    
    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text= "Score:{}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_mov, snake, food)

def change_direction(new_direction):
    global direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]
    
    if x<0 or x>= WIDTH:
        return True

    elif y<0 or y>=HEIGHT:
        return True
    
    for len in snake.coordinates[1:]:
        if x == len[0] and y == len[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       text = "GAME_OVER",
                       font= ("calibri",60),
                       fill= 'red',
                       tag= 'gameover' )

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_heigth/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Left>', lambda event: change_direction('left'))

snake = Snake()
food = Food()

next_mov(snake, food)

window.mainloop()
