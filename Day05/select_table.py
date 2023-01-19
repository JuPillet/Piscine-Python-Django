from urllib import response
import psycopg2

if __name__ == '__main__':
	conn = psycopg2.connect(
		database = 'djangotraining',
		host = 'localhost',
		user = 'djangouser',
		password = 'secret'
		)
	
	curr = conn.cursor()

	curr.execute( """ select * from Members """ )
	response = curr.fetchall()
	for row in response :
		print( row )
	conn.close()