class HotBeverage:
	price = 0.30
	name = "hot beverage"

	def description( self ):
		return "Just some hot water in a cup."

	def __str__( self ):
		return """name : """ + self.name + """
price : %.2f""" % self.price + """
description : """ + self.description()

class	Coffee( HotBeverage ):
	name = "coffee"
	price = 0.40

	def description( self ):
		return "A coffee, to stay awake."

class	Tea( HotBeverage ):
	name = "tea"

	def description( self ):
		return  "Just some hot water in a cup."

class	Chocolate( HotBeverage ):
	name = "chocolate"
	price = 0.50

	def description( self ):
		return  "Chocolate, sweet chocolate..."

class	Cappuccino( HotBeverage ):
	name = "cappuccino"
	price = 0.45

	def description( self ):
		return  "Un po’ di Italia nella sua tazza!"

def beverages():
	hot_beverage = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()

	print()
	print( hot_beverage )
	print()
	print( coffee )
	print()
	print( tea )
	print()
	print( chocolate )
	print()
	print( cappuccino )

if __name__ == "__main__":
	beverages()