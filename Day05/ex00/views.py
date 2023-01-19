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

		curr.execute( """ CREATE TABLE IF NOT EXISTS ex00_movies (
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