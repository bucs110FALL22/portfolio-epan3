import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.screensize()
#makes turtle screen full screen found online stackOverflow
window.setup(width=1.0, height=1.0, startx=None, starty=None)
window.bgcolor('lightblue')


michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#generating random distance for turtles
random_distance = random.randrange(1,100)
random_distance1 = random.randrange(1,100)

#moving turtles forward
michelangelo.forward(random_distance)
leonardo.forward(random_distance1)
#resetting their position
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#generating new distances for each turtle
new_distance = random.randrange(0,10)
new_distance1 = random.randrange(0,10)

#using range for for loop
for i in range(10):
  michelangelo.forward(new_distance)
  leonardo.forward(new_distance1)
  
#resetting their position
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# #click on screen to start Part B
# window.exitonclick()

# PART B - complete part B here
#setup for pygame and display
pygame.init()
window = pygame.display.set_mode()
  
#colors rgb (r,g,b) codes
black = (0, 0, 0)
pink = (255, 0, 225)
red = (255, 0, 0)
aquamarine = (126,255,212)
blue = (0, 0, 255)
green = (28, 224, 25)
white = (255, 255, 255)

#settings variables for triangle
coords = []
num_sides = 3
side_length = 100
offset = 120

# calculating coordinates for triangle
for i in range(3):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += ((x,y),)

#drawing equilateral triangle
window.fill(black)
pygame.draw.polygon(window, pink, coords)
pygame.display.update()
pygame.time.wait(1000)

# setting new variables for square
coords = []
num_sides = 4
side_length = 100
offset = 120

# calculating coordinates for square
for i in range(4):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += ((x,y),)

#drawing square
window.fill(black)
pygame.draw.polygon(window, red, coords)
pygame.display.update()
pygame.time.wait(1000)

#settings new variables for hexagon
coords = []
num_sides = 6
side_length = 100
offset = 120

# calculating coordinates for hexagon
for i in range(6):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += ((x,y),)

#drawing hexagon
window.fill(black)
pygame.draw.polygon(window, blue, coords)
pygame.display.update()
pygame.time.wait(1000)

#setting new variables for nonagon
coords = []
num_sides = 9
side_length = 100
offset = 120

# calculating coordinates for nonagon
for i in range(9):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += ((x,y),)

#drawing nonagon
window.fill(black)
pygame.draw.polygon(window, green, coords)
pygame.display.update()
pygame.time.wait(1000)

#setting new variables for circle
coords = []
num_sides = 360
side_length = 100
offset = 120

# calculating coordinates for circle
for i in range(360):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += ((x,y),)

#drawing circle
window.fill(black)
pygame.draw.polygon(window, aquamarine, coords)
pygame.display.update()
pygame.time.wait(1000)

#pygame looping code so it won't close found online
#make sure to click on the 'X' to close the program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
#make sure to click on the 'X' to close the program

#shorter loop for shapes but doesn't change color
# for x in [3,4,6,9,360]:
#   num_sides = x
#   coords = []
#   side_length = 100
#   offset = 120
#   for i in range(x):
#     theta = (2.0 * math.pi * i) / num_sides
#     x = side_length * math.cos(theta) + offset
#     y = side_length * math.sin(theta) + offset
#     coords += ((x,y),)
#   window.fill(black)
#   pygame.draw.polygon(window, pink, coords)
#   pygame.display.update()
#   pygame.time.wait(3000)

##### Figured out how to change color in loop for shapes
# #variable for changing colors in if statements
# count = 0

# for x in [3,4,6,9,360]:
#   num_sides = x
#   coords = []
#   side_length = 100
#   offset = 120
#   for i in range(x):
#     theta = (2.0 * math.pi * i) / num_sides
#     x = side_length * math.cos(theta) + offset
#     y = side_length * math.sin(theta) + offset
#     coords += ((x,y),)
#   window.fill(black)
#   if count == 0:
#     pygame.draw.polygon(window, pink, coords)
#   elif count == 1:
#     pygame.draw.polygon(window, red, coords)
#   elif count == 2:
#     pygame.draw.polygon(window, blue, coords)
#   elif count == 3:
#     pygame.draw.polygon(window, green, coords)
#   elif count == 4:
#     pygame.draw.polygon(window, aquamarine, 
#     coords)
#   pygame.display.update()
#   pygame.time.wait(3000)
#   count += 1

# # window.exitonclick()

#In case I need the things below I'll leave them here
### Prior work for [Part A]:
# for i in [angle] * num_sides:
#   my_turtle.forward(length)
#   my_turtle.left(i)
#for loop

# for i in [new_distance1] * 10:
#   michelangelo.forward(i)
#   leonardo.forward(i)
#not sure if its suppose to be this fast

# for i in [new_distance] * 10:
#   michelangelo.forward(i)
#   leonardo.forward(i)

#--------------------------------------#

### Prior hard coded work for [Part B]:

# x = side_length * math.cos(theta) + offset
# y = side_length * math.sin(theta) + offset
# coords = x+y
# print(coords)
# theta = (2.0 * math.pi * side_length) / num_sides
# print(theta)

# #shapes coordinates
# triangle = [(110,175),(200,20),(290,175)]
# square = [(150,50),(150,150),(250,150),(250,50)]
# #circle coordinates below
# center = (200,100)
# radius = 80
# width = 300
# hexagon = [(235,35),(271,97),(235,159),(163,159),(127,97),(163,35)]
# nonagon = [(200,164),(160,148),(135,109),(143,65),(177,36),(223,36),(257,65),(265,110),(242,148)]

# #drawing circle
# window.fill(black)
# pygame.draw.circle(window, aquamarine, center, radius, width)
# pygame.display.update()
# pygame.time.wait(3000)