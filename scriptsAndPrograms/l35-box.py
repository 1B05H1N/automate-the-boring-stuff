"""

*************************
*						*
*						*
*						*
*************************


"""

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception("The symbol needs to be a string length of 1")
	print(symbol * width)

	for i in range (height - 2):
		print(symbol + (" " * (width - 2)) + symbol)

	print(symbol * width)

boxPrint("*", 15, 5)
boxPrint("o", 40, 7)
