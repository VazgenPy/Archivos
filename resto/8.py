nombre = input("Dime el archivo: ")
archivo = open("a" + nombre + ".txt" , "r")
b = archivo.read()


def contar(file):
	lista = b.split()
	contar = len(file.split())
	escritura = open("a5.txt" , "w")
	escritura.write("El numero de palabras es: " + str(contar) + "\n")
	escritura.close()
	return(lista)
	

def se_repite(lista):
	frecuencia = []
	for w in lista:
		frecuencia.append(lista.count(w))
	a = frecuencia.index(max(frecuencia))
	escritura = open("a5.txt" , "a")
	escritura.write("La palabra que mas se repite es: " + str(lista[a]) + "\n")
	escritura.close()
	return(lista)


def numero_de_palabras(lista):
	c = list(set(lista))
	for i in c:
		escritura = open("a5.txt" , "a")
		escritura.write("la palabra " + str(i) + " se repite " + str(lista.count(i)) + " veces " + "\n")
		escritura.close()


numero_de_palabras(se_repite(contar(b)))

