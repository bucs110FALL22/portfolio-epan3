import random

#generating random number
number = random.randrange(1,10)

#variables
attempt = 0

#asking user for input
guess = input("Guess the random number: ")
guess = int(guess)

#while loop for guessing game
while guess != number:
  if guess < number:
    print("Too Low.")
    guess = input("Guess the random number: ")
    guess = int(guess)
    attempt += 1
  elif guess > number:
    print("Too High.")
    guess = input("Guess the random number: ")
    guess = int(guess)
    attempt += 1
attempt += 1

#if it satisfies while loop then prints correct
print("Correct!")
#prints number of attempts it took the user
print ("You guessed the number in", attempt, "tries.")