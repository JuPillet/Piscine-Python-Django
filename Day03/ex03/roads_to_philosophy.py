import requests as req
import bs4
from bs4 import BeautifulSoup
import sys

def	request_wikipedia():
#	try:
		if sys.argv.__len__() != 2:
			raise Exception( "one argument is required as subject of your search." )
		subject = sys.argv[1]
		page = subject.capitalize().replace( " ", "" ) + ".wiki"

		url = 'https://en.wikipedia.org/wiki/' + subject

		response = req.get(url)
		response = BeautifulSoup( response.text, 'html.parser' )
		index = 0
		for line in response:
			if index == 2:
				response = line
				break
			index += 1
		index = 0
		str( bs4.element.Tag( response ) )
#		for line in response:
#			print( line )
#			if index == 2:
#				break
#			index += 1
#		if response['error']:
#			raise Exception( str( response['error']['info'] ).replace( 'The page', 'The page "' + subject + '"' ) )
#	except Exception as err:
#		print( "Error:", err )

if __name__ == "__main__":
	request_wikipedia()