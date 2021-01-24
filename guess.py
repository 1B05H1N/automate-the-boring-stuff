#this is a guess the number game

import random

print("Hello, what is your name?")
name = input()

print("Well," + name + ", I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1,20)

#print("Debug: the secret number is " + str(secretNumber))

for guessesTaken in range(1,7):
	print("Take a guess.")
	guess = int(input())

	if guess < secretNumber:
		print("Your guess is too low.")
	elif guess > secretNumber:
		print("Your guess is too high.")
	else:
		break # this condition is for the correct guess!

if guess == secretNumber:
	print(("Good job, ") + name + ("! You guessed the number in ") + srt(guessesTaken) + ("guesses!"))
else:
	print("Nope, the number was " + str(secretNumber) + (" !"))

print("You took " + str(guessesTaken) + " guesses.")