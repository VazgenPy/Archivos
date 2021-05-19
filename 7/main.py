import os
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
	print("Bienvenido a mi programa vas a disfrutar de una experiencia bastante educativa, empecemos!")
	opcion = ""
	while opcion != "5":
		opcion = input('''1. Search | 2. Continent | 3. Esperanza | 4. Ayuda | 5. Exit
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
			print("""Hola si has entrado aqui es porque necesitas ayuda

1. Search: Esta opcion sirve para buscar los datos basicos de un pais.

2. Continent: Esta opcion sirve para buscar los paises, la poblacion y la superficie del continente que quieras.

3. Esperanza: Esta opcion sirve para buscar el nombre de un pais segun su Renta Per Capita y su Esperanza de Vida.
			""")
			input()
			cls()
			continue
		elif opcion == "5":
			print("\tAdios amigo mio nos veremos luego!")
			exit()
		else:
			cls()


def datos(lista):
	a = input("\tDime el nombre del pais: ")
	b = input("\t\tLo quieres escribir o añadir? ")
	for i in lista:
		for j in range(len(i)):
			if i[j] == a:
				if b == "escribir":
					for x in range(len(i)):
						print("\n\t\t\t" + lista[0][x] + ": " + str(i[x]))
					break
				elif b == "añadir":
					for w in range(len(i)):
						arch = open("7/" + i[j] + ".txt", "a" , encoding = "utf-8")
						arch.write("\n" + lista[0][w] + ": " + str(i[w]) + "\n")
						arch.close()
					break
			

def continente(lista):
	population = 0
	surface = 0
	a = input("\tDime el continente: ")
	opcion = input("Que quieres escribir o añadir: ")
	if opcion == "escribir":
		for i in lista:
			for j in range(len(i)):
				try:
					if i[j] == a:
						print(i[1])
						population = population + i[6]
						surface = surface + i[4]
						break
				except:
					continue
		print("Superficie: " , surface , " habitantes" , "Poblacion: " , population , " Km^2")
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
	a = "{:.2f}".format(float(input("Dime la renta per capita: ")))
	b = float(input("Dime la esperanza de vida: "))
	c = input("Lo quieres añadir o escribir: ")
	for i in range(1 , len(lista)):
		try:
			if a == "{:.2f}".format(lista[i][8] / lista[i][6]):
				if b == lista[i][7]:
					if c == "escribir":	
						print(lista[i][1] , "," , "{:.2f}".format(lista[i][8] / lista[i][6]) , "," , lista[i][7])
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