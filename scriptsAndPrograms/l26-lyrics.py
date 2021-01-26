import re 

lyrics = ("""On the twelfth day of Christmas, my true love sent to me, 12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and A partridge in a pear tree""")

xmasRegex = re.compile(r'\d+\s\w+')
xmas = xmasRegex.findall(lyrics)

print(xmas)

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall("Robocop shot the baby food in the movie")
print(vowels)

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
doubleVowels = vowelRegex.findall("Robocop shot the baby food in the movie")
print(doubleVowels)

consonantsRegex = re.compile(r"[^aeiouAEIOU]")
consonants = consonantsRegex.findall("Robocop shot the baby food in the movie")
print(consonants)