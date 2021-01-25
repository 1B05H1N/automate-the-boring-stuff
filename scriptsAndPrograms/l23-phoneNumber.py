def isPhoneNumber(text):
	if len(text) != 12:
		return False #not the right phone number length
	for i in range(0,3):
		if not text[i].isdecimal():
			return False #no area code
	if text[3] != "-":
		return False #missing dash
	for i in range(4,7):
		if not text[i].isdecimal():
			return False #no first 3 digits
	if text[7] != "-":
		return False #missing second dash
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False #missing last 4 digits
	return True

print(isPhoneNumber('818-555-1234'))
print(isPhoneNumber('hello'))

message = "Call me at 818-555-1234 tomorrow, or at 818-555-9999 for my office phone"
foundNumber = False
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print("Phone number found: " + chunk)
		foundNumber = True
if not foundNumber:
	print("Could not find any phone numbers.")

import re

phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumberRegex.search(message)
print(mo.group())
no = phoneNumberRegex.findall(message)
print(no)