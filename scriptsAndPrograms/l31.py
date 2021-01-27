helloFile = open("..\\textFile\\helloworld.txt")
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open("..\\textFile\\helloworld.txt")
lines = helloFile.readlines()
print(lines)
helloFile.close()

helloFile = open("..\\textFile\\helloworld2.txt", "w")
helloFile.write("Hello there!!!!")
helloFile.close()

appleFile = open("..\\textFile\\apple.txt", "w")
appleFile.write("Apples are not vegetables")

appleFile = open("..\\textFile\\apple.txt", "a")
appleFile.write("\n\nApples are delicious!")

import shelve
shelfFile = shelve.open("mydata")
shelfFile["cats"] = ["cat1","cat2","cat3"]
shelfFile.close()

shelfFile = shelve.open("mydata")
shelfFile["cats"]
shelfFile.close()

shelfFile = shelve.open("mydata")
shelfFile.keys()
list(shelfFile.keys())

list(shelfFile.values())

