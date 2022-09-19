import random

#generating random number
number = random.randrange(1,11)

#variables
attempt = 0
correct_guess = False

for i in range(3):
  #asking user for input
  guess = input("Guess the random number: ")
  guess = int(guess)
  attempt += 1
  if guess < number:
    print("Too Low.")
  elif guess > number:
    print("Too High.")
  else:
    print("Correct!")
    print("It took you", attempt, "attempts to get it correct")
    break


