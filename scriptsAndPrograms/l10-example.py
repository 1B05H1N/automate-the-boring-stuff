spam = 42 # global variable

def eggs():
	spam = 42 # local variable 

print("Some code.")
print("More code. \n")

def spam_():
	eggs_ = 99
	bacon()
	print(eggs_)

#spam()
#print(eggs) # local variables can't be used in the global scope 

def bacon():
	ham = 101
	eggs_ = 0

spam_() # local scopes cannot refer to local scopes of another function

def spamm():
	#global eggs
 	eggss = "Hello"
 	print(eggss)

eggss = 42
spamm()
print(eggs)