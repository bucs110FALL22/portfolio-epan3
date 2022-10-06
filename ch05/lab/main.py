### Part A
# variables
n = 101
count = 0

# while loop for 3n+1
while n != 1:
  if (n % 2) == 0:
    count += 1
    print('\neven')
    n /= 2
    print(n)
  elif (n % 2) == 1:
    count += 1
    print('\nodd')
    n = (n * 3) + 1
    print(n)

# printing results
print('\nn is equal to ', n)
print('The program has stopped...')
print('The value of count is', count)

###-----------------------------###

print('\n---------------------------')

### Part B
# variables
upper_limit = 21 # changed upper limit to 21 since range(2,20) doesn't include 20
iters = {} # an empty dictionary
num = 0 # num is the new count variable for part B
attempt = 0 # tracking each new value (ex: attempt 1, value 2, attempt 2, value 3, etc...)

# for loop
for start in range(2, upper_limit):
  num = 0 # resets count to 0 again
  attempt += 1
  value = start # sets the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
  print("\nAttempt #{}:".format(attempt))
  while start != 1:
    print("\nStart #: {}".format(start))
    if (start % 2) == 0:
      num += 1
      print('Result: even')
      start /= 2
      print('Current: {}'.format(start))
    elif (start % 2) == 1:
      num += 1
      print('Result: odd')
      start = (start * 3) + 1
      print('Current: {}'.format(start))
  iters[value] = num

# storing in iters in a new variable same as shown in instructions
threeplus1_iters_dict=iters

# printing entire dictionary for 3n + 1 for {value:num,value:num...value:num}
print(threeplus1_iters_dict)

### Part C
# import pygame
import pygame

# initialize pygame
pygame.init()

# creating display
display = pygame.display.set_mode()

# settings colors
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]

# vairables
upper_limit = 21
iters = threeplus1_iters_dict
max_so_far = 0
max_val = 0
scale = 5

# iters = zip(iters.values(), iters.keys())
pairs = [(x, y) for (x, y) in iters.items()]
print(pairs)

# fill the screen with color
display.fill(black)

# drawing graph
pygame.draw.lines(display, green, False, pairs)
new_display = pygame.transform.flip(display, False, True)
new_display = pygame.transform.scale(new_display, (500,500))
new_display.blit(new_display, (0, 0))
pygame.display.update()

# setting font
font = pygame.font.Font(None, 20)
msg = font.render("test", False, "blue")
display.blit(msg, (10,10))
pygame.display.update()

# for loop
for n in range(2, upper_limit):
  pygame.display.update()
  num = 0 # resets count to 0 again
  attempt += 1
  value = n # sets the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
  while n != 1:
    if (n % 2) == 0:
      num += 1
      n /= 2
    elif (n % 2) == 1:
      num += 1
      n = (n * 3) + 1
  iters[value] = num
print(iters)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()