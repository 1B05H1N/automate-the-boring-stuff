list("Hello")

name = "Sophie"
name[0]

name[1:3]
name[-2]

"Zo" in name
"xxx" in name

tuple([1,2,3])
list([1,2,3])

spam = 42
cheese = spam
spam = 100
spam

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = "Hello!"
cheese 

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
newName

import copy

spam = ["A", "B", "C", "D"]
cheese = copy.deepcopy(spam)
cheese = [1] = 42
cheese

spam = ["apples",
		"oranges",
		"bananas",
		"cats"]

print("Four score and seven" + \
	"years ago")

print("Four score and seven" + "years ago")