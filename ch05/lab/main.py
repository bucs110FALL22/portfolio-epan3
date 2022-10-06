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

# print results
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
attempt = 0 # track each new value (ex: attempt 1, value 2, attempt 2, value 3, etc...)

# for loop
for start in range(2, upper_limit):
  num = 0 # reset count to 0 again
  attempt += 1
  value = start # set the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
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

# store iters in a new variable as shown in instructions
threeplus1_iters_dict = iters

# print entire dictionary for 3n + 1 for {value:num,value:num...value:num}
print("\n",threeplus1_iters_dict)

### Part C
# import pygame
import pygame

# initialize pygame
pygame.init()

# create display
display = pygame.display.set_mode()

# set colors
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]

# variables
upper_limit = 21
iters = threeplus1_iters_dict
max_so_far = 0
max_val = 0
scale = 14
new = {}

# fill the screen with background color
display.fill(black)

# for loop for 3n+1 [2,20] (inclusive)
for n in range(2, upper_limit):
  pygame.display.update()
  num = 0 # reset count to 0 again
  attempt += 1
  value = n # set the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
  # loop stops at n = 1 and statements inside check for even or odd #s
  while n != 1:
    if (n % 2) == 0:
      num += 1
      n /= 2
    elif (n % 2) == 1:
      num += 1
      n = (n * 3) + 1
  iters[value] = num
  # compare max_so_far with num, update max_val & max_so_far variables
  if max_so_far < num:
    max_val = value
    max_so_far = num
    print (f'Max Value: {max_val}\nMax So Far: {max_so_far}')

  # new dictionary puts compared values above in it
  new[max_val] = max_so_far
  # printing new dictionary
  print(new)

  # convert dictionary coordinates to listed tuples
  pairs = [(x * scale, y * scale) for (x, y) in iters.items()]
  
  # drawing graph
  new_display = pygame.Surface(display.get_size())
  pygame.draw.lines(new_display, green, False, pairs)
  new_display = pygame.transform.flip(new_display, False, True)
  display.blit(new_display, (0, 0))
  pygame.display.update()

  # set string with on screen text message
  max_value_string = f'Max Value: {max_val}   Max So Far: {max_so_far}'

  # render string variable to display on screen
  font = pygame.font.Font(None, 20)
  msg = font.render(max_value_string, False, white)
  display.blit(msg, (0,0))
  pygame.display.update()
  pygame.time.wait(1000)

# program runs continuously; closes when user presses 'X'
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()