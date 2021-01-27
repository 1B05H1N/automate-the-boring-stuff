import os
import shutil
import send2trash

os.getcwd()
os.unlink("file.txt")
os.rmdir("directory.txt")\
shutil.rmtree("..\\directory")

send2trash.send2trash("..\\directory\\directory.txt")