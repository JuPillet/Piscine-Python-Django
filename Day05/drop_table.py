import psycopg2

if __name__ == '__main__':
	conn = psycopg2.connect(
		database = 'djangotraining',
		host = 'localhost',
		user = 'djangouser',
		password = 'secret'
	)
	curr = conn.cursor()
	curr.execute(""" DROP TABLE ex02_movies """)
	conn.commit()
	conn.close()