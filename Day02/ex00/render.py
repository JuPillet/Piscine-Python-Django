import sys
import os
import re
import settings as settings

def	render():
	try:
		if sys.argv.__len__() == 2:
			if sys.argv[1].endswith(".template") == -1:
				raise Exception( "document as argument is not a '.template' extention." )
		else:
			raise Exception( "program want only one document as argument." )
		html = re.sub( "template$", "html", sys.argv[1] )
		ofile = open( html, "w" )
		with open( sys.argv[1], "r" ) as ifile:
			ofile.write( settings.opener )
			for line in ifile:
				line = re.sub("{name}", settings.name, line)
				line = re.sub("{surname}", settings.surname, line)
				line = re.sub("{age}", settings.age, line)
				line = re.sub("{profession}", settings.profession, line)
				line = re.sub("{.*?}", '', line)
				ofile.write( "\t\t" + line )	
			ofile.write( settings.closer )
		ofile.close()
	except Exception as err:
		print( "Error:", err )

if __name__ == "__main__":
	render()
	