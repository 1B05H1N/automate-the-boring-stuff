import re
beginsWithHelloRegex = re.compile(r"^Hello")
begin = beginsWithHelloRegex.search("Hello there!")
print(begin)

beginsWithHelloRegex.search('He said "Hello!"')
beginCondition = beginsWithHelloRegex.search('He said "Hello!"') == None
print(beginCondition)

endsWithWorldRegex = re.compile(r"world!$")
endsWith = endsWithWorldRegex.search("Hello world!")
print(endsWith)

endsWithWorldRegex.search("Hello world!")

allDigitsRegex = re.compile(r'^\d+$')
y = allDigitsRegex.search('123541785491813412')
x = allDigitsRegex.search('123412431234b3124132431')
print(x,y)

atRegex = re.compile(r'.at')
suess = atRegex.findall('The cat in the hat sat on the flat mat.')
print(suess)

atRegex = re.compile(r' .{1,2}at')
dot = atRegex.findall('The cat in the hat sat on the flat mat.')
print(dot)

# .* == anything

"First name: Al Last NameL Sweigart".find(":") + 2
"First name: Al Last NameL Sweigart"[12:]

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall("First name: Al Last NameL Sweigart")

serve = "<To serve humans> for dinner.>"

nongreedy = re.compile(r'<(.*?)>')
non = nongreedy.findall(serve)
print(non)

greedy = re.compile(r'<(.*)>')
veryGreedy = greedy.findall(serve)
print(veryGreedy)

prime = 'Serve the public trust. \nProtect the innocent.\nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
dotDot = dotStar.search(prime)
print(dotDot)

dotStar = re.compile(r'.*', re.DOTALL)
dotDotStar = dotStar.search(prime)
print(dotDotStar)

vowelRegex = re.compile(r'[aeiou]')
search = vowelRegex.search("Al, why does your programming book talk about Robocop so much?")
find = vowelRegex.findall("Al, why does your programming book talk about Robocop so much?")
print(search, find)

vowelRegex = re.compile(r'[aeiou]', re.I)
find2 = vowelRegex.findall("Al, why does your programming book talk about Robocop so much?")
print(find2)