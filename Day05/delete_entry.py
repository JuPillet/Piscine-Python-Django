import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect = psycopg2.connect(
						database = 'djangotraining',
						host = 'localhost',
						user = 'djangouser',
						password = 'secret'
						)

curr = conn.cursor()

curr.execute( """ delete from Members where lastname like 'Clapton' """ )
conn.commit()
conn.close()