cat = {"name": "Zophie", "age":7, "color":"gray"}
allCats = []

cat = {"name": "Zophie", "age":7, "color":"gray"}
cat = {"name": "Pooka", "age":5, "color":"black"}
cat = {"name": "Fat-Tail", "age":7, "color":"gray"}
cat = {"name": "???", "age":-17, "color":"orange"}

theBoard = {"top-l": " ", "top-M": " ", "top-R": " ", 
"mid-L": " ", "mid-M": "X", "mid-R": " ",
"low-L": " ", "low-M": " ", "low-R": " "}

import pprint
pprint.pprint(theBoard)

theBoard["mid-M"] = " "

pprint.pprint(theBoard)

theBoard["mid-M"] = "X"
pprint.pprint(theBoard)

theBoard["top-l"] = "O"
theBoard["top-M"] = "O"
theBoard["top-R"] = "O"
theBoard["mid-L"] = "X"
theBoard["low-R"] = "X"

pprint.pprint(theBoard)

def printBoard(board):
	print(board["top-l"] + "|" + board["top-M"] + "|" + board["top-R"])
	print("-----")
	print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
	print("-----")
	print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
	
printBoard(theBoard)

type(42)
type("hello")
type(3.14)
type(theBoard)
type(theBoard["top-R"])
