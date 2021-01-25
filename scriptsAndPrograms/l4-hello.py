# this program says hello and asks for your name

print("Hello World!")

print("What is your name?")
myName = input()
print("It's good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))

print("What's your age in years?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year or so!")


"""recap:
type program files into the file editor
the execution starts at the top and moves down
# comments are ignored by python
functions are mini-programs in your program
print() displays the value passed to it
input() lets the user type in the value
len() takes a string value and returns an integer value of the string's length
int(), str(), and float() convert values' data type"""