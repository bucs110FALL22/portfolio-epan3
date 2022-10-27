import turtle

# maximizes turtle screen size
def fullscreen(window = None, width = 0, height = 0, startx = None, starty = None):
  window.setup(width, height, startx, starty)
  window.bgcolor('black')

def moon(turtle = None, color=None, xcoord=0, ycoord=0, size=0):
  turtle.up()
  turtle.goto(xcoord,ycoord)
  turtle.color(color)
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
  turtle.goto(xcoord+20,ycoord)
  turtle.color('black')
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  turtle.hideturtle()

def star(turtle = None, color = None, loop = 0, units = 0, angle = 0):
  turtle.color(color)
  turtle.begin_fill()
  for i in range(loop):
    turtle.forward(units)
    turtle.right(angle)
  turtle.end_fill()

def cloud(turtle = None, color = None, loop = 0, units = 0, size = 0):
  turtle.color(color)
  for i in range(loop):
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(units)
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
  
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

def fireworks(turtle = None, color = None, units = 0, loop = 0):
  for i in range(loop):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(units)
    turtle.left(170)
    turtle.forward(units)
    turtle.end_fill()
    turtle.hideturtle()
  
def redfireworks(turtle,color):
  return fireworks(turtle,color,16,19)

def bluefireworks(turtle,color):
  return fireworks(turtle,color,16,19)

def greenfireworks(turtle,color):
  return fireworks(turtle,color,16,19)

def main():
  screen = turtle.Screen()
  screen.screensize()
  fullscreen(screen, width = 1.0, height = 1.0, startx=None, starty=None)

  coby = turtle.Turtle()
  
  COLORS = ['#4287f5','#9ed7ff','#fcec03','#FF0000','#00fffb','#00ff51','#ffd900']
  SIZE = [20,40]
  UNITS = [60,100,16,10]
  ANGLE = [90,174,144]
  XCOORD = -180
  YCOORD = 80
  LOOP = [19,5]

  moon(coby, COLORS[6], XCOORD, YCOORD, SIZE[1]) 
  coby.goto(-120,120)
  star(coby, COLORS[6], LOOP[1], UNITS[3],ANGLE[2])

  coby.setpos(140,100)
  cloud(coby, "white", LOOP[1], UNITS[3], SIZE[0])
  
  coby.speed(300)
  circle(coby, COLORS[0], UNITS[1])
  letter(coby, COLORS[1], SIZE[0], UNITS[0], ANGLE[0])

  coby.setpos(-10,80)
  coby.speed(300)
  fireworks(coby,COLORS[2],UNITS[2],LOOP[0])

  coby.speed(300)
  coby.setpos(-10,-86)
  redfireworks(coby,COLORS[3])

  coby.speed(300)
  coby.setpos(-80,0)
  bluefireworks(coby,COLORS[4])
  
  coby.speed(300)
  coby.setpos(80,0)
  greenfireworks(coby,COLORS[5])

  screen.exitonclick()
main()