class Hola:
	a = input("Hola Dime tu nombre: ")
	def change_name(self , new_name):
		self.a = new_name
		return(self.a)

Hola = Hola() 

print(Hola.a)

print(Hola.change_name("AJAJAJAJAJAJ"))

