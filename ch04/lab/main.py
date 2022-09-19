#importing modules
import random
import pygame
import math

#setup for pygame and display
screen_width = 228
screen_height = 246

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

#circular dart coordinates below
center = (115,112)
radius = 113.5
width = 300
xline = [(110,226),(110,110),(110,-1)]
yline = [(0,110),(200,110),(400,110)]

#changing title
pygame.display.set_caption("Dart Game")

#Part A)
#drawing dartboard
window.fill(blue)
pygame.draw.circle(window, red, center, radius, width)
pygame.draw.polygon(window, black, xline)
pygame.draw.polygon(window, black, yline)
pygame.display.update()

#Part B)
for i in range(10):
  #random dart (x,y) dar values
  dartx = random.randrange(0,screen_width)
  darty = random.randrange(0,screen_height)
  #settings variables to draw circle
  center1 = (dartx,darty)
  radius1 = 2.5
  center1 = (dartx,darty)
  #determining if lands in circle
  xdistance = screen_width - dartx
  ydistance = screen_height - darty
  distance_from_center = math.hypot(xdistance, ydistance)
  screen_size = (screen_width * screen_height) / 2
  is_in_circle = distance_from_center <= screen_size
  not_in_circle = distance_from_center > screen_size
  if is_in_circle:
    pygame.draw.circle(window, green, center1, radius1, width)
    pygame.display.update()
  else:
    pygame.draw.circle(window, yellow, center1, radius1, 
    width)
    pygame.display.update()
  
  
#pygame looping code so it won't close found online
#make sure to click on the 'X' to close the program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()