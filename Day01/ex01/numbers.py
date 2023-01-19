def	put_numbers():
	with open( "numbers.txt", 'r' ) as f:
		result = 0
		for line in f:
			for character in line:
					if ( character != ',' and character != '\n' ):
						result = result * 10 + int( character )
					else:
						print( result )
						result = 0

if __name__ == '__main__':
	put_numbers()