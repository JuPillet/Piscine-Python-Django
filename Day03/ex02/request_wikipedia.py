import requests as req
import json as jso
import dewiki as de
import sys

def	request_wikipedia():
	try:
		if sys.argv.__len__() != 2:
			raise Exception( "one argument is required as subject of your search." )
		subject = sys.argv[1]
		page = subject.capitalize().replace( " ", "" ) + ".wiki"

		url = 'https://fr.wikipedia.org/w/api.php'
		params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
			'prop': 'wikitext'
    	}

		response = req.get(url, params = params).json()
		if response['error']:
			raise Exception( str( response['error']['info'] ).replace( 'The page', 'The page "' + subject + '"' ) )
		response = response['parse']['wikitext']['*']
		response = de.from_string( response )
		page = open( page, "w" )
		page.write( response )
		page.close()
	except Exception as err:
		print( "Error:", err )

if __name__ == "__main__":
	request_wikipedia()