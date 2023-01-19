import psycopg2

if __name__ == '__main__':
	conn = psycopg2.connect(
			database = 'djangotraining',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
		)

	curr = conn.cursor()

	curr.execute( """
			INSERT INTO Members ( firstname, lastname, birthdate) VALUES
			('Eric', 'Clapton', '1945-03-30'),
			('Joe', 'Bonamassa', '1977-05-08')
			""" )

	conn.commit()
	conn.close()