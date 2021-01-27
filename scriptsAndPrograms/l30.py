'c:\\spam\\eggs.png'

print('\\')

print(r'c:\spam\eggs.png')

'\\'.join(['folder','folder2', 'file.png'])

import os
#os.path.join(['folder','folder2', 'file.png'])

os.sep

os.getcwd()

os.chdir('c:\\')

os.getcwd()

'c:\\folder1\\spam.png' #absolute
'\folder1\\spam.png' #relative

os.chdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.5")

os.path.abpath('spam.png')

os.path.abspath("..\\..\\spam.png")

os.path.isabs("c:\\folder\\folder")

os.path.relpath("c:\\folder1\\folder2\\spam.png", "c:\\folder1")

os.path.dirname("c:\\folder1\\folder2\\spam.png")

os.path.basename("c:\\folder1\\folder2\\spam.png")

os.path.basename("c:\\folder1\\folder2")

os.path.exists("c:\\folder1\\folder2\\spam.png")

os.path.exist("c\\windows\\system32\\calc.exe")

os.path.dir("c\\windows\\system32\\calc.exe")

os.path.dir("c\\windows\\system32")

os.path.getsize("c\\windows\\system32\\calc.exe")

os.listdir("c\\windows\\system32")

os.makedirs("C:\\delicious\\walnut\\waffles")