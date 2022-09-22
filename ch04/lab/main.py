#importing modules
import random
import pygame
import math

#setup for pygame and display
screen_width = 468
screen_height = 225

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))

#getting window size
x, y = window.get_size()

#checking window size
print(x,y)

#colors
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255, 255, 0)

#blue player circular dart coordinates below
center = (115,112)
radius = 113.5
width = 300
xline = [(110,226),(110,110),(110,-1)]
yline = [(0,110),(200,110),(456,110)]

#red player circulate dart coordinates below
square = [(234.7,0),(466.9,0),(466, 229.4),(234.7, 229.4)]
center1 = (350,112)
radius1 = 113.5
width1 = 300
xline1 = [(350,226),(350,110),(350,-1)]

#changing title
pygame.display.set_caption("Dart Game")

#Part A)
#drawing blue player dartboard
window.fill(blue)
pygame.draw.circle(window, red, center, radius, width)
pygame.draw.polygon(window, black, xline)
pygame.draw.polygon(window, black, yline)
pygame.display.update()

#drawing red player backboard and dartboard
pygame.draw.polygon(window, red, square)
pygame.draw.circle(window, blue, center1, radius1, width1)
pygame.draw.polygon(window, black, xline1)
pygame.draw.polygon(window, black, yline)
pygame.display.update()

#Part B)
#blue player dart for loop
dartWidth = 0
for i in range(10):
  #random dart (x,y) dart values
  dartx = random.randrange(0,228)
  darty = random.randrange(0,225)
  #settings variables to draw circle
  center1 = (dartx,darty)
  radius1 = 2.5
  center1 = (dartx,darty)
  #determining if lands in circle
  xdistance = dartx - 115
  ydistance = darty - 112
  distance_from_center = math.hypot(xdistance, ydistance)
  screen_size = radius#(screen_width * screen_height) / 2
  is_in_circle = distance_from_center <= screen_size
  not_in_circle = distance_from_center > screen_size
  if is_in_circle:
    pygame.draw.circle(window, green, center1, radius1, dartWidth)
    pygame.display.update()
    pygame.time.wait(500)
  else:
    pygame.draw.circle(window, yellow, center1, radius1, 
    dartWidth)
    pygame.display.update()
    pygame.time.wait(500)

#red player dart for loop
dartWidth = 0
for i in range(10):
  #random dart (x,y) dart values
  dartx = random.randrange(234,466)
  darty = random.randrange(0,229)
  #settings variables to draw circle
  center1 = (dartx,darty)
  radius1 = 2.5
  center1 = (dartx,darty)
  #determining if lands in circle
  xdistance = dartx - 350
  ydistance = darty - 112
  distance_from_center = math.hypot(xdistance, ydistance)
  screen_size = radius#(screen_width * screen_height) / 2
  is_in_circle = distance_from_center <= screen_size
  not_in_circle = distance_from_center > screen_size
  if is_in_circle:
    pygame.draw.circle(window, green, center1, radius1, dartWidth)
    pygame.display.update()
    pygame.time.wait(500)
  else:
    pygame.draw.circle(window, yellow, center1, radius1, 
    dartWidth)
    pygame.display.update()
    pygame.time.wait(500)

    

#Part C)




#pygame looping code so it won't close found online
#make sure to click on the 'X' to close the program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()