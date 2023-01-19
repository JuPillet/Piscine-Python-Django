import psycopg2

if __name__ == '__main__':
	conn = psycopg2.connect(
		database = 'djangotraining',
		host = 'localhost',
		user = 'djangouser',
		password = 'secret'
		)

	curr = conn.cursor()

	curr.execute( """ CREATE TABLE Members (
				id serial PRIMARY KEY,
				firstname varchar(32),
				lastname varchar(32),
				birthdate date
				)
				""" )

	conn.commit()
	conn.close()