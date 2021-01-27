import shutil
shutil.copy("..\\helloworld.txt", "..\\recap")
shutil.copy("..\\helloworld.txt", "..\\garbage.txt")

shutil.copytree("..\\textFile", "..\\recap")

shutil.move("..\\helloworld.txt", "..\\automate-the-boring-stuff")

shutil.move("..\\helloworld.txt", "..\\automate-the-boring-stuff\\hello.txt")