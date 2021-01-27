import os

totalSize = 0
for filename in os.listdir("C:\\automate-the-boring-stuff"):
	if not os.path.isfile(os.path.join("C:\\automate-the-boring-stuff", filename)):
		continue 
	totalSize = totalSize + os.path.getsize(os.path.join("C:\\automate-the-boring-stuff", filename))
print(totalSize)