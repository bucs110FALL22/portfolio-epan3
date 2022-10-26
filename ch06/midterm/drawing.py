import turtle

# maximizes turtle screen size
def fullscreen(window = None, width = 0, height = 0, startx = None, starty = None):
  window.setup(width, height, startx, starty)
  window.bgcolor('black')

# draws letter E
def letter(turtle=None, color = None, size = 0, units = 0, angle = 0):
  # puts pen on paper & sets position (x, y) coordinates
  turtle.pendown()
  turtle.setpos(-30, 60)

  # setting size & color
  turtle.pensize(size)
  turtle.color(color)

  # for loop for four parts of letter E
  for i in range(2):
    turtle.forward(units)
    turtle.backward(units)
    turtle.right(angle)
    turtle.forward(units)
    turtle.left(angle)

  # draws last segment: '_' 
  turtle.forward(units)
  turtle.penup()

def circle(turtle = None, color = None, units = 0):
  turtle.color(color)
  turtle.begin_fill()
  turtle.penup()
  turtle.setpos(-2,-100)
  turtle.pendown()
  turtle.circle(units)
  turtle.end_fill()
  
def main():
  screen = turtle.Screen()
  screen.screensize()
  fullscreen(screen, width = 1.0, height = 1.0, startx=None, starty=None)

  COLORS = ['#4287f5','#9ed7ff']
  SIZE = 20
  UNITS = [60,100]
  ANGLE = 90
  coby = turtle.Turtle()

  circle(coby, COLORS[0], UNITS[1])
  letter(coby, COLORS[1], SIZE, UNITS[0], ANGLE)

  screen.exitonclick()
main()