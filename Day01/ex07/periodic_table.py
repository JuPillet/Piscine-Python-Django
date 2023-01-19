def css_format():
	ofile = open( "style.css", "w" )
	ofile.write(
"""body {
	width: 1024;
	height: 860;
}

table {
	max-width: 1024;
	max-height: 860;
	width: 100%;
	height: 100%;
	border-collapse: collapse;
}

td {
	padding-left: 1%;
	padding-right: 1%;
	margin-left: 1%;
	margin-right: 1%;
}

.elem {
		border:3px solid #000000;
}

ul {
	list-style:none;
	padding-left: 0;
	padding-right: 0;
}

li {
	font-size: 0.6em;
}
	""" )
	ofile.close()

class Elem:
	def	__init__( self, elem_split ):
		self.name = elem_split[0].split(" = ")[0]
		self.position = int( ( ( ( ( elem_split[0] ).split(" = ") )[1] ).split( ":" ) )[1] )
		self.number = int( elem_split[1].split(":")[1] )
		self.small = elem_split[2].split(": ")[1]
		self.molar = elem_split[3].split(":")[1]
		self.electron = elem_split[4].split(":")[1]

def	gen_open_html( ofile ):
	ofile.write( """<!DOCTYPE html>
<html lang="en">""" )

def	gen_head( ofile ):
	ofile.write( """
	<head>
		<meta charset="UTF-8">
		<title>Mendeleiev’s Table</title>
		<meta name="Description" content="periodic table">
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>""" )

def	gen_open_tbody( ofile ):
	ofile.write( """
	<body>
		<table>
			<tbody>""" )

def	gen_tr_table( elem_list, ofile ):
	def	gen_table_td_blank():
		ofile.write("""
					<td></td>""" )
	def	gen_table_td( elem = Elem ):
		ofile.write("""
					<td class="elem">
						<ul>
							<li><h4>""" + elem.name + """</h4></li>
							<li>No""" + str(elem.number) + """</li>
							<li>""" + elem.small + """</li>
							<li>""" + elem.molar + """</li>
							<li>""" + elem.electron + """ electron</li>
						</ul>
					</td>""" )
	elem = 1
	while elem < elem_list.__len__() :
		ofile.write( """
				<tr>""" )
		column = 0
		while column < 18:
			if elem_list[elem].position == column:
				gen_table_td( elem_list[elem] )
				elem += 1
			else:
				gen_table_td_blank()
			column += 1
		ofile.write( """
				</tr>""" )

def	gen_close_tbody_html( ofile ):
	ofile.write( """
			</tbody>
		</table>
	</body>
</html>""" )


def	periodic_table():
	def gen_dict():
		with open( "periodic_table.txt", "r" ) as ifile:
			elem_list = dict( { int: Elem } )
			index = 1
			for	line in ifile:
				elem = Elem( line.split(", ") )
				elem_list[index] = elem
				index += 1
		return elem_list
	elem_list = gen_dict()

	ofile = open( "periodic_table.html", "w" )
	gen_open_html( ofile )
	gen_head( ofile )
	gen_open_tbody( ofile )
	gen_tr_table( elem_list, ofile )
	gen_close_tbody_html( ofile )
	ofile.close()

if __name__ == "__main__":
	css_format()
	periodic_table()
