import time
import os
import sys
from datetime import date


ESO1 = []
ESO2 = []
ESO3 = []
ESO4 = []
BAT1 = []
BAT2 = []


def cls():
    os.system("cls" if os.name=="nt" else "clear")


while True:
	directorio = input("Dime el directorio del archivo de matricula: ")
	if (os.path.isdir(directorio)):
		if (os.path.isfile(directorio + "alumnat.csv")):
			print("Es un directorio ")
			cls()
			break
		else:
			cls()
			input("El archivo no esta en ese directorio")
			cls()
	else:
		input("No es un directorio")
		cls()


archivo = open(directorio + "alumnat.csv" , "r")
read = archivo.readlines()
lista = []
lista_nueva = []


def UI():
	print("Hola bienvendio a la copia barata de DINANTIA")
	opcion = ""
	while opcion != "5":
		opcion = input('''1. Pasar Lista | 2. Consultar Assistencia | 3. Borrar los datos de los alumnos | 4. Ayuda | 5. Salir
''')
		if opcion == "1":
			passar_llista()
			continue
		elif opcion == "2":
			consultar_assistencia()
			continue
		elif opcion == "3":
			borrar_todos_los_datos()
			continue
		elif opcion == "4":
			cls()
			print('''1. Pasar Lista: Sirve para crear archivos en los que dice si el alumno ha faltado o no.

2. Consultar Assistencia: Sirve para ver que alumno ha faltado o no, segun su curso.

3. Borrar los datos de los alumnos: Sirve para eliminar los datos de los alumnos

4. Si pones "*" y pulsas ENTER vuelves atras. NOTA: Solo funciona si estas en la opcion de consultar asistencia

5. Salir
''')
			input()
			cls()
			continue
		elif opcion == "5":
			exit()
		else:
			cls()
			continue

def archivo_alumnat():
	for i in read:
		lista.append(i.split(","))
	for i in range(len(lista)):
		lista_nueva.append([lista[i][0] , lista[i][2] , lista[i][5]])
	for i in range(1 , len(lista_nueva)):
		if lista[i][1] == "11" or lista[i][1] == "12":
			ESO1.append(lista_nueva[i])
		elif lista[i][1] == "13":
			ESO2.append(lista_nueva[i])
		elif lista[i][1] == "14":
			ESO3.append(lista_nueva[i])
		elif lista[i][1] == "15":
			ESO4.append(lista_nueva[i])
		elif lista[i][1] == "16":
			BAT1.append(lista_nueva[i])
		elif lista[i][1] >= "17":
			BAT2.append(lista_nueva[i])


def passar_llista():
	while True:
		cls()
		assistencia = input("Dime el drectorio donde quieres guardar los archivos de los alumnos: ")
		cls()
		registre = input("Dime el directorio donde quieres guardar el registro de la lista: ")
		cls()
		if os.path.isdir(assistencia) and os.path.isdir(registre):
			input("Los directorios se han localizado con EXITO!")
			cls()
			break
		else:
			print("Alguno de los directorios no existe por favor vuelve a intentarlo")
	a = ["ESO1" , "ESO2" , "ESO3" , "ESO4" , "BAT1" , "BAT2"]
	w = 0
	for j in (ESO1 , ESO2 , ESO3 , ESO4 , BAT1 , BAT2):
		for i in j:
			arch = open(assistencia + a[w] + ".txt" , "a")
			arch.write(" | ".join(i))
			arch.close
		w = w+1
	curs = input("De que curso quieres pasar lista: ")
	cls()
	archivo = open(assistencia + curs + ".txt" , "r").readlines()
	for i in archivo:
		i = i.split(" | ")
		print(i[0])
		while True:
			asist = input("Ha asistido? (1 si , 0 no): ")
			if asist == "1" or asist == "0":
				cls()
				break
			else:
				input("No puedes poner eso")
				cls()
				print(i[0])
		archivo_de_assistencia = open(registre + curs + str(date.today()) + ".txt" , "a")
		archivo_de_assistencia.write(str(i[0]) + " - " + str(asist) + "\n---------------------------------\n")
		archivo_de_assistencia.close()


def consultar_assistencia():
	cls()
	while True:
		directorio = input("Dime el directorio: ")
		if os.path.isdir(directorio):
			break
		elif directorio == "*":
			cls()
			return()
		else:
			input("Ese directorio no existe")
			cls()
	fichero = os.listdir(directorio)
	cls()
	print(fichero)
	opcion_curso = input("Que curso quieres: ")
	cls()
	archivo = open(directorio + opcion_curso + ".txt" , "r").readlines()
	for i in archivo:
		i = i.split(" - ")
		try:
			if i[1] == "0\n":	
				print(i[0] , "----> FALTA!!!")
			else:
				print(i[0])
		except:
			continue
	input()
	cls()


def borrar_todos_los_datos():
	cls()
	dir = input("Dime el directorio de los archivos que quieres borrar: ")
	lista_de_archivos = ["ESO1" , "ESO2" , "ESO3" , "ESO4" , "BAT1" , "BAT2"]
	for i in (lista_de_archivos):
		if os.path.exists(dir + i + ".txt"):
			os.remove(dir + i + ".txt")
	cls()
	input("Todos los archivo han sido eliminados de su PC con exito :)")
	cls()


archivo_alumnat()

UI()