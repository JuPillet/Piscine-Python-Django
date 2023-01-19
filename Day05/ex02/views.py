from django.http import HttpResponse
import psycopg2
from django.shortcuts import render

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

		curr.execute( """ CREATE TABLE IF NOT EXISTS ex02_movies (
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
		return render( request, 'init.html', { 'result': 'OK' } )
	except Exception as err:
		conn.close()
		return render( request, 'init.html', { 'result': "ERROR: " + str( err ) } )

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
				INSERT INTO ex02_movies ( title, episode_nb, opening_crawl, director, producer, release_date ) VALUES
				('""" + film[1] + "', '" + film[0] + "', '', '" + film[2] + "', '" + film[3] +"', '" + film[4] + """')""" )	
			conn.commit()
			result.append( 'OK' )
		conn.close()
		return render( request, 'populate.html', { "result": result } )
	except Exception as err:
		conn.close()
		result.append( "ERROR: " + str( err ) )
		return render( request, 'init.html', { "result": result } )
	
def	display( request ):
	try:
		result = []
		conn = psycopg2.connect(
			database = 'djangotraining',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)

		curr = conn.cursor()

		curr.execute( """ select * from ex02_movies """ )
		response = curr.fetchall()
		for row in response :
			column = []
			for col in row:
				column.append( col )
			result.append( column )
		conn.close()
		return render( request, 'display.html', { "result": result } )
	except Exception as err:
		conn.close
		return render( request, 'init.html', { "result": "Error: " + str( err ) } )