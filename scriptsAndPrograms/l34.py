import os
os.walk("..\\automate-the-boring-stuff")
for folderName, subfolders, filenames in os.walk("..\\automate-the-boring-stuff"):
	print("The folder is " + folderName)
	print("The subfolders are " + folderName + " are: " + str(subfolders))
	print("The filenames in " + folderName + " are: " + str(filenames)

	for subfolder in subfolders:
		if "fish" in subfolder:
			os.rmdir(subfolder)

	for file in filenames:
		if file.endswith(".py"):
			shutil.copy(os.join(folderName, file), os.join(folderName) + ".backup")
