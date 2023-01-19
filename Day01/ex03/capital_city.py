import sys

def	capital_city():
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

	if sys.argv[1] in states:
		link = states[sys.argv[1]]
		return str( capital_cities[link] )
	return str( '' )

if __name__ == "__main__":
	if sys.argv.__len__() == 2:
		answer = capital_city()
		if not answer:
			answer = str( "Unknown state" )
		print( answer )