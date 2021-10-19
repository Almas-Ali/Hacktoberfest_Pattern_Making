import turtle

t = turtle.Turtle()
t.speed(0)
def spiral(val): 
  for i in range(36): #draw the circle of squares
   t.forward(val)
   t.right(90)
   t.forward(val)
   t.right(90)
   t.forward(val)
   t.right(90)
   t.forward(val)
   t.right(100)
  for i in range(100): #draw the spiral inside the circle of squares
   t.forward(i)
   t.right(80)   

spiral(200)


