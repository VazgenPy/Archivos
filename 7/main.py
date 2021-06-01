import time
import os
import sys
archivo = open("7/country.csv", "r" , encoding = "utf-8")
read = archivo.readlines()
lista = []


def cls():
    os.system("cls" if os.name=="nt" else "clear")


def lectura_de_archivo(file):
	for i in read:
		i = i.replace('"', "")
		lista.append(i.split(","))
	for linea in lista:
		for j in range(len(linea)):
			try:
				linea[j] = float(linea[j])
			except:
				pass
	return(lista)


def UI():
	intro = """Bienvenido a mi programa vas a disfrutar de una experiencia bastante educativa
Controles: ENTER PARA CONTINUAR
ADELANTE!"""
	for i in intro:
		print(i , end='')
		sys.stdout.flush()
		time.sleep(0.025)
	input()
	cls()
	opcion = ""
	while opcion != "5":
		opcion = input('''1. Buscar | 2. Continente | 3. Renta y Esperanza | 4. Ayuda | 5. Exit
''')
		if opcion == "1":
			datos(lista)
			input()
			cls()
			continue
		elif opcion == "2":
			continente(lista)
			input()
			cls()
			continue
		elif opcion == "3":
			esperanza(lista)
			input()
			cls()
			continue
		elif opcion == "4":
			cls()
			print("""Hola si has entrado aqui es porque necesitas ayuda

1. Buscar --> Esta opcion sirve para buscar los datos basicos de un pais.

2. Continente --> Esta opcion sirve para buscar los paises, la poblacion y la superficie del continente que quieras.

3. Renta y Esperanza --> Esta opcion sirve para buscar el nombre de un pais segun su Renta Per Capita y su Esperanza de Vida.

Diviertete :)
			""")
			input()
			cls()
			continue
		elif opcion == "5":
			cls()
			print("Adios amigo mio nos veremos luego!")
			exit()
		else:
			cls()


def datos(lista):
	cls()
	a = input("Dime el nombre del pais, el Codigo o el nombre Local: ")
	b = input("\n\tLo quieres escribir o añadir? ")
	for i in lista:
		for j in range(len(i)):
			if i[j] == a:
				if b == "escribir":
					for x in range(len(i)):
						print("\n\t\t" + lista[0][x] + ": " + str(i[x]))
					break
				elif b == "añadir":
					for w in range(len(i)):
						arch = open("7/" + i[j] + ".txt", "a" , encoding = "utf-8")
						arch.write(lista[0][w] + ": " + str(i[w]) + "\n\n")
						arch.close()
					break
		

def continente(lista):
	cls()
	population = 0
	surface = 0
	a = input("Dime el continente: ")
	opcion = input("\n\tQue quieres escribir o añadir: ")
	if opcion == "escribir":
		for i in lista:
			for j in range(len(i)):
				try:
					if i[j] == a:
						print("\n\t\t" + i[1])
						population = population + i[6]
						surface = surface + i[4]
						break
				except:
					continue
		print("\n\t\tSuperficie: " + str(surface) + " Km^2" + "\n\n\t\tPoblacion: " + str(population) + " habitantes")
	elif opcion == "añadir":
		for i in lista:
			for j in range(len(i)):
				try:
					if i[j] == a:
						population = population + i[6]
						surface = surface + i[4]
						arch = open("7/" + a + ".txt" , "a")
						arch.write(i[1] + "\n")
						arch.close()
				except:
					continue
		arch = open("7/" + a + ".txt" , "a")
		arch.write("Poblacion: " + str(population) + " habitantes" + "\n" + "Superficie: " + str(surface) + " Km^2")
		arch.close()	


def esperanza(lista):
	cls()
	a = "{:.2f}".format(float(input("Dime la renta per capita: ")))
	b = float(input("\n\tDime la esperanza de vida: "))
	c = input("\n\t\tLo quieres añadir o escribir: ")
	for i in range(1 , len(lista)):
		try:
			if a == "{:.2f}".format(lista[i][8] / lista[i][6]):
				if b == lista[i][7]:
					if c == "escribir":	
						print("\n\t\t\t" , lista[i][1] , "\n\n\t\t\t\tRenta per capita: " , "{:.2f}".format(lista[i][8] / lista[i][6]) , "\n\n\t\t\t\t\tEsperanza de vida: " , lista[i][7])
						break
					elif c == "añadir":
						arch = open("7/" + lista[i][1] + "_Esperanza" + ".txt" , "a")
						arch.write(lista[i][1] + " , " + str("{:.2f}".format(lista[i][8] / lista[i][6])) + " , " + str(lista[i][7]))
						arch.close()
						break
		except:
			continue
		
						

lectura_de_archivo(archivo)


for i in lista[0]:
	for j in range(len(i)):	
		if i[j] == "\n":
			lista[0].remove("Code2\n")
			lista[0].append("Code2")


UI()