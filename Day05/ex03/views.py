from django.shortcuts import render
from ex03.models import Movies

# Create your views here.
def populate( request ):
	result = []
	movies = [
		['1', 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'],
		['2', 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'],
		['3', 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'],
		['4', 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'],
		['5', 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'],
		['6', 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'],
		['7', 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11']
	]
	try:
		for film in movies:
			movie = Movies( film[1], film[0], '', film[2], film[3], film[4] )
			movie.save()
			result.append( 'OK' )
		return render( request, 'populate.html', { "result": result } )
	except Exception as err:
		result.append( "ERROR: " + str( err ) )
		print( result )
		return render( request, 'init.html', { "result": result } )
	
def	display( request ):
	result = []
	try:
		movies = Movies.objects.all()
		for row in movies :
			column = [ row.title, row.episode_nb, row.opening_crawl, row.director, row.producer, row.release_date  ]
			result.append( column )
		return render( request, 'display.html', { "result": result } )
	except Exception as err:
		return render( request, 'init.html', { "result": "Error: " + str( err ) } )