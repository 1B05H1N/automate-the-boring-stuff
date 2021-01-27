import os

os.chdir("..\\automate-the-boring-stuff")
for filename in os.listdir():
	if filename.endswith(".txt"):
		#os.unlink(filename)
		print(filename)