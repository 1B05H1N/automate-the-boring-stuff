print(list(range(50,100,10)))

supplies = ["pens", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
	print("Index " + str(i) + " in supplies list is " + supplies[i])

cat = ["fat", "orange", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat

size, color, disposition = "skinny", " black", "quiet"
a = "AAA"
b = "BBB"
a, b = b, a

spam = 42
spam = spam + 1
spam += 1