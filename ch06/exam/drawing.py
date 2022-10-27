# imports
import turtle

# maximizes turtle screen size
def fullscreen(window = None, width = 0, height = 0, startx = None, starty = None):
  window.setup(width, height, startx, starty)
  window.bgcolor('#051b55')

# function drawing moon
def moon(turtle = None, color = None, xcoord = 0, ycoord = 0, size = 0):
  turtle.penup()
  turtle.goto(xcoord,ycoord)
  turtle.color(color)
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
  turtle.goto(xcoord+20,ycoord)
  turtle.color('#051b55')
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  turtle.hideturtle()

# function drawing star
def star(turtle = None, color = None, loop = 0, units = 0, angle = 0):
  turtle.color(color)
  turtle.begin_fill()
  for i in range(loop):
    turtle.forward(units)
    turtle.right(angle)
  turtle.end_fill()

# function drawing cloud
def cloud(turtle = None, color = None, loop = 0, units = 0, size = 0):
  turtle.color(color)
  for i in range(loop):
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(units)
    turtle.circle(size+i)
    size -= i
    turtle.end_fill()
    turtle.penup()

# function drawing icon
def circle(turtle = None, color = None, units = 0):
  turtle.color(color)
  turtle.begin_fill()
  turtle.penup()
  turtle.setpos(-2,-100)
  turtle.pendown()
  turtle.circle(units)
  turtle.end_fill()
    
# function drawing letter E
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

# function drawing fireworks
def fireworks(turtle = None, color = None, units = 0, loop = 0):
  for i in range(loop):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(units)
    turtle.left(170)
    turtle.forward(units)
    turtle.end_fill()
    turtle.hideturtle()

# function drawing red fireworks (by returning fireworks())
def redfireworks(turtle = None, color = None):
  return fireworks(turtle,color,16,19)

# function drawing blue fireworks (by returning fireworks())
def bluefireworks(turtle = None, color = None):
  return fireworks(turtle,color,16,19)

# function drawing green fireworks (by returning fireworks())
def greenfireworks(turtle = None, color = None):
  return fireworks(turtle,color,16,19)

  def text(turtle = None):
    turtle.write("Eric Pan", True, align = "center")
    turtle.write((-50,-50), True)

# main function
def main():
  # creating a screen object
  screen = turtle.Screen()
  screen.screensize()

  # adjusting to full screen
  fullscreen(screen, width = 1.0, height = 1.0, startx=None, starty=None)

  # creating turtle object
  coby = turtle.Turtle()

  # CONSTANT variables for all functions
  COLORS = ['#4287f5','#9ed7ff','#fcec03','#FF0000','#00fffb','#00ff51','#ffd900']
  SIZE = [20,40]
  UNITS = [60,100,16,10]
  ANGLE = [90,174,144]
  XCOORD = -180
  YCOORD = 80
  LOOP = [19,5]

  # adjusting turtle speed
  coby.speed(7)
  
  # drawing moon
  moon(coby, COLORS[6], XCOORD, YCOORD, SIZE[1]) 

  # setting position & drawing star
  coby.setpos(-120,120)
  star(coby, COLORS[6], LOOP[1], UNITS[3],ANGLE[2])

  # setting position & drawing cloud
  coby.setpos(140,100)
  cloud(coby, "white", LOOP[1], UNITS[3], SIZE[0])

  # speeding up drawing
  coby.speed(8)

  # drawing circular icon
  circle(coby, COLORS[0], UNITS[1])

  # drawing letter E on top of icon
  letter(coby, COLORS[1], SIZE[0], UNITS[0], ANGLE[0])

  # speeding up drawing
  coby.speed(300)
  
  # setting position & drawing fireworks  
  coby.setpos(-10,80)
  fireworks(coby,COLORS[2],UNITS[2],LOOP[0])

  coby.setpos(-10,-86)
  redfireworks(coby,COLORS[3])

  coby.setpos(-80,0)
  bluefireworks(coby,COLORS[4])
  
  coby.setpos(80,0)
  greenfireworks(coby,COLORS[5])

  # waits for user to click before closing 
  screen.exitonclick()
main()