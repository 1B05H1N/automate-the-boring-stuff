#! python3

# This program was created in the automate the boring stuff with python udemy course created by al swiegart
# This program will take phone numbers and emails on your clipboard and output them in a nice format
# This program requires pyperclip which can be installed with 'pip install pyperclip'

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 818-000-0000, 000-0000, (818) 000-0000, 000-0000 ext 12345, ext.12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?			# area code(optional)
(\s|-)				# first separator
\d\d\d				# first 3 digits
-					# separator
\d\d\d\d			# last 4 digits
(((ext(\.)?\s)|x)		# extension (optional)
(\d{2-5}))?			# extension number-part (optional)
)
''', re.VERBOSE	)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r"""
# some.+_thing@something(\d{2,5}))?.com

[a-zA-Z0-9_.+]+		# name part
@					# @ symbol
[a-zA-Z0-9_.+]+		# domain name part

""", re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

#print(extractedPhone, extractedEmail)

# TODO: Copy the extracted email/phone to the clipboard
result = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(result)
print(result)