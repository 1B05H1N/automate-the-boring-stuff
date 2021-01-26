import re 
namesRegex = re.compile(r'Agent \w+')
namesRegex.findall("Agent Alice gave the secret documents to Agent Bob")
redacted = namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
print(redacted)

namesRegex = re.compile(r'Agent (\w)\w*')
redacted2 = namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
print(redacted2)

redacted3 = namesRegex.sub(r"Agent \1*****", "Agent Alice gave the secret documents to Agent Bob.")
print(redacted3)

re.compile(r'''
	(\d\d\d-) | 	# area code (without parens, with dash)
	(\(\d\d\d\) ) 	# -or- area code with parens and no dash 			
	\d\d\d 			# first 3 digits
	-				#second dash
	\d\d\d\d 		# last 4 digits
	\sx\d{2,4}		# extentions, like x1234''', re.VERBOSE)

re.compile(r'''
	(\d\d\d-) | 	# area code (without parens, with dash)
	(\(\d\d\d\) ) 	# -or- area code with parens and no dash 			
	\d\d\d 			# first 3 digits
	-				#second dash
	\d\d\d\d 		# last 4 digits
	\sx\d{2,4}		# extentions, like x1234''', re.IGNORECASE)

re.compile(r'''
	(\d\d\d-) | 	# area code (without parens, with dash)
	(\(\d\d\d\) ) 	# -or- area code with parens and no dash 			
	\d\d\d 			# first 3 digits
	-				#second dash
	\d\d\d\d 		# last 4 digits
	\sx\d{2,4}		# extentions, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)