from random import randrange
import beverages as bev

class CoffeeMachine():
	def	__init__( self ):
		self.drink = 10

	class	EmptyCup( bev.HotBeverage ):
		name = "empty cup"
		price = 0.90
		def	description( self ):
			return "An empty cup?! Gimme my money back!"

	class	BrokenMachineException( Exception ):
		def __init__( self ):
			raise Exception( "This coffee machine has to be repaired." )

	def	repair( self ):
		self.drink = 10
	
	def serve( self, choise ):
		choises = {
			"hot beverage": bev.HotBeverage(),
			"coffee": bev.Coffee(),
			"tea": bev.Tea(),
			"chocolate": bev.Chocolate(),
			"cappuccino": bev.Cappuccino()
		}
		try:
			if not self.drink:
				self.BrokenMachineException()
			command = choises.get( choise )
			if type( command ) is not type( None ):
				self.drink -= 1
				if randrange(1, 100) > 66:
					return self.EmptyCup()
				return command
			else:
				return "Command " + choise + " unknown"
		except Exception as err:
			print( err )


def	machine():
	menu = """Menu:
- hot beverage
- coffee
- tea
- chocolate
- cappuccino

Choose your drink: """

	machine = CoffeeMachine()
	print( "Machine will turn on. Welcome customer!!!" )
	print()
	while True:
		try:
			select = input( menu ).casefold()
			if select == "exit":
				print( "Machine will turn off. See you later!!!" )
				break
			if select == "repair":
				if machine.drink:
					print( "Machine work correcly! Call the reparator is useless!" )
					print()
				else:
					machine.repair()
					print( "Machine work again" )
					print()
			else:
				select = machine.serve( select )
				if select != None:
					print( select )
				print()
		except:
			print()

if __name__ == "__main__":
	machine()