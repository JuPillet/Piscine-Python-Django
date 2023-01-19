import sys

def	capital_city( searched ):
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

	for state in states:
		if state.casefold() == searched:
			return list( {capital_cities[states[state]], state} )
	return None

def	state( searched ):
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
		if link in capital_cities and capital_cities[link].casefold() == searched :
			return list( {capital_cities[link], state} )

	return None

if __name__ == "__main__":
	searched = str()
	if sys.argv.__len__() == 2:
		for character in sys.argv[1]:
			if character != ',':
				searched += character
			else:
				searched = searched.strip()
				if searched.__len__():
					answer = capital_city( searched.casefold() )
					if answer == None:
						answer = state( searched.casefold() )
						if answer == None:
							print( searched, "is neither a capital city nor a state" )		
						else:
							print( answer[0], "is the capital of", answer[1] )			
					else:
						print( answer[0], "is the capital of", answer[1] )
				searched = str()