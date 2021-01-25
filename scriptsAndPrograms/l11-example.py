def div42by(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print("Error: You can't divide by zero.", end="...")

print(div42by(20))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print("How many cats do you have?")
numCats = input()
try:
	if int(numCats) >= 4:
		print("That's a lot of cats!")
	else:
		print("That's not many cats...")
except ValueError:
	print("You did not enter a number.")