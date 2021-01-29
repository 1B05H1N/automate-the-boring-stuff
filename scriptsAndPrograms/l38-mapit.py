import webbrowser, sys, pyperclip

#webbrowser.open("https://ibo.network")

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# check is command line arguments were passed
if len(sys.argv) > 1:
	# ['mapit.py', '870', 'Valencia', 'St.'] - > '870 Valencia St.'
	address = ' '.join.(sys.argv[1:])
else:
	address = pyperclip.paste()

# htts://www.gogole.com/maps/place/<ADDRESS>
webbrowser.open('htts://www.gogole.com/maps/place/' + address)