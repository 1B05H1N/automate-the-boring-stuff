market_2nd = {"ns": "green", "ew":"red"}

def swtichLights(intersection):
	for key in intersection.keys():
		if intersection[key] == 'green':
			intersection[key] = 'yellow'
		if intersection[key] == 'yellow':
			intersection[key] = 'red'
		if intersection[key] == 'red':
			intersection[key] = 'green'
	assert 'red' in intersection.values(), "Neither light is red" + str(intersection)

print(market_2nd)
swtichLights(market_2nd)
print(market_2nd)