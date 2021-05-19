import os
matricula = open("matricula.csv" , "r")
lista = matricula.readlines()


def cls():
	os.system("cls" if os.name == "nt" else "clear")


def crear(nombre):
	directorio = input("En que directorio lo quieres guardar? ")
	if os.path.exists(directorio):
		pass
	else:
		cls()
		crear(input("Dime el nombre del estudiante: (Pepe , Luis , Fernando): "))
		exit()


	for linea in lista: 
		a = linea.split(",")
		if a[0] == nombre:	
			archivo = open(directorio + a[0] + ".md" , "w")
			archivo.write("## " + a[0] + " Ha sido matriculado en: \n-" + "\n-".join(a[1:]))
			archivo.close()
		

crear(input("Dime el nombre del estudiante: (Pepe , Luis , Fernando): "))