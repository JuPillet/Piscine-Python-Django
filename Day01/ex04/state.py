import sys

def	state():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for	state in states:
		link = states[state]
		if link in capital_cities and capital_cities[link] == sys.argv[1]:
			return state
	return ( '' )

if __name__ == "__main__":
	if sys.argv.__len__() == 2:
		answer = state()
		if not answer:
			answer = str( "Unknown state" )
		print( answer )