listaDeLineas = []
lista_sin_repeticion = []


def Existe(nombre):
	numero = 0
	resultado = []
	for i in range(len(listaDeLineas)):
		if nombre == listaDeLineas[i][0]:
			a = i
			numero = numero + 1
			resultado.append(int(listaDeLineas[i][1]))
	if numero >= 1:
		lista_sin_repeticion.append(listaDeLineas[a][0])
		lista_sin_repeticion.append(sum(resultado))
		return(lista_sin_repeticion)


def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:
		for i in range(len(fila)):
			if fila[i] == " ":
				listaDeLineas.append([fila[0:i],fila[i+1]])



for j in [1,2,3]:
	lecturaArchivos("a"+str(j)+".txt")

for i in ["Juan" , "Gonzalo" , "Fran" , "Luis"]:
	Existe(str(i))


print(listaDeLineas)


print(lista_sin_repeticion)

lista_para_averiguar_el_ganador = []

for i in [1,3,5,7]:
	lista_para_averiguar_el_ganador.append(lista_sin_repeticion[i])

puntuaje = min(lista_para_averiguar_el_ganador)

ubicacion = lista_sin_repeticion.index(puntuaje)

print("El ganador es" , lista_sin_repeticion[ubicacion - 1])