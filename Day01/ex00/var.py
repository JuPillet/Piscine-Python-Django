

def	my_var():
	def print_var( my_param ):
		print( my_param, "has type", type(my_param) )

	var1 = int(42)
	print_var(var1)

	var2 = str( "42" )
	print_var(var2)

	var3 = str( "quarante-deux" )
	print_var(var3)

	var4 = float( 42.0 )
	print_var(var4)

	var5 = bool( True )
	print_var(var5)

	var6 = list([42])
	print_var(var6)

	var7 = dict({42: 42})
	print_var(var7)

	var8 = tuple([42,])
	print_var(var8)

	var9 = set()
	print_var(var9)

if __name__ == '__main__':
	my_var()
	