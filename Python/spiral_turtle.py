import turtle as t

class Spiral:
  def __init__(self):
    self.colors = ['red', 'cyan', 'green', 'yellow', 'white', 'orange']
    self.bg_color = 'black'
    self.speed = 0
    self.line_count = 200
    
  def draw(self, bg_color: str):
    t.bgcolor(bg_color)
    for lines in range(self.line_count):
      t.pencolor(self.colors[lines%len(self.colors)])
      t.width(lines/101)
      t.forward(lines)
      t.left(59)
    
    t.hideturtle()
    t.done()
    
if __name__ == '__main__':
  spiral = Spiral()
  print('begin drawing...')
  spiral.draw(spiral.bg_color)
  print('done')