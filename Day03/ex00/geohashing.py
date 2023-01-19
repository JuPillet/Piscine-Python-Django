import sys
from antigravity import geohash

def	geohashing():
	try:
		if sys.argv.__len__() != 5:
			raise Exception( "4 argument required for geoashin.py: one floting longitute, one floating latitude, one date message formated like YYYY-MM-DD and one floating index based one the walstreat dow opening" )
		longi		= float( sys.argv[1] )
		lati		= float( sys.argv[2] )
		date		= str( sys.argv[3] )
		index		= float( sys.argv[4] )
		encoded		= ( date + '-' + str( index ) ).encode()
		geohash( longi, lati, encoded )
	except Exception as err:
		print( err )

if __name__ == "__main__":
	geohashing()