import psycopg2
from django.shortcuts import render, get_object_or_404
from ex04.models import Movies

# Create your views here.
def	init( request ):
	try:
		conn = psycopg2.connect(
			database = 'djangotraining',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
		)

		curr = conn.cursor()

		curr.execute( """ CREATE TABLE IF NOT EXISTS ex04_movies (
				title varchar(64) not null unique,
				episode_nb bigserial PRIMARY KEY,
				opening_crawl text not null,
				director varchar(32) not null,
				producer varchar(128) not null,
				release_date date not null
				)
				""" )

		conn.commit()
	
		conn.close()
		return render( request, 'table_added.html', { 'result': 'OK', } )

	except Exception as err:
		return render( request, 'table_added.html', { 'result': err } )

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
		conn = psycopg2.connect(
			database = 'djangotraining',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
		)

		curr = conn.cursor()
		for film in movies:
			curr.execute( """
				INSERT INTO ex04_movies ( title, episode_nb, opening_crawl, director, producer, release_date ) VALUES
				('""" + film[1] + "', '" + film[0] + "', '', '" + film[2] + "', '" + film[3] +"', '" + film[4] + """') ON CONFLICT (episode_nb) DO NOTHING""" )	
			conn.commit()
			result.append( 'OK' )
		conn.close()
		return render( request, 'populate.html', { "result": result } )
	except Exception as err:
		conn.close()
		result.append( "ERROR: " + str( err ) )
		return render( request, 'init.html', { "result": result } )

def	display( request ):
	result = []
	try:
		movies = Movies.objects.all()
		if not movies.__len__():
			raise Exception()
		for row in movies :
			column = [ row.title, row.episode_nb, row.opening_crawl, row.director, row.producer, row.release_date  ]
			result.append( column )
		return render( request, 'display.html', { "result": result } )
	except Exception:
		return render( request, 'init.html', { "result": "Error: No data available" } )

def	remove( request ):
	result = []
	try:
		curr = conn.cursor()

		if request.method == 'POST':
			conn = psycopg2.connect = psycopg2.connect(
				database = 'djangotraining',
				host = 'localhost',
				user = 'djangouser',
				password = 'secret'
				)
			title = request.POST.get( "titles_list" )
			print( title )
			curr.execute( "delete from Movies where lastname like " + title )
			conn.commit()
			conn.close()
		movies = Movies.objects.all()
		if not movies.__len__():
			raise Exception()
		movies = Movies.objects.all()
		for row in movies :
			result.append( row.title )
		return render( request, 'remove.html', { "result": result } )
	except Exception:
		return render( request, 'init.html', { "result": "Error: No data available" } )