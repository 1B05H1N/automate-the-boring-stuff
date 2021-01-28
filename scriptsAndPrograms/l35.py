raise Exception("This is an error message.")

import traceback 

try:
	raise Exception("This is an error message.")

except:
	errorFile = open("..\\scriptsAndPrograms\\error_log.txt", "a")
	errorFile.write(traceback.format_exec())
	errorFile.close()
	print("The traceback info was written to error_log.txt")

import os
os.getcwd()

assert False, "This is the error message."

