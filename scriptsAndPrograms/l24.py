import re
phoneNumberRegex = re.compile(r"\d\d\d\-\d\d\d-\d\d\d\d")
phoneNumberRegex.search("My number is 818-555-1234")

mo = phoneNumberRegex.search("My number is 818-555-1234")
mo.group()

phoneNumberRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
no = phoneNumberRegex.search("My number is 818-555-1234")
print(no.group())
print(no.group(1))
print(no.group(2))

phoneNumberRegex = re.compile(r"\(\d\d\d\) \d\d\d-\d\d\d\d")
mo = phoneNumberRegex.search("My number is 818-555-4242")
mo = phoneNumberRegex.search("My number is (818) 555-4242")
print(mo.group())

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
mo.group()

mo = batRegex.search("Batmotorcycle lost a wheel")
mo == None

mo = batRegex.search("Batmotorcycle list a wheel")
#mo.group() #this will not work!