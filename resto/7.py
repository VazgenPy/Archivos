listaDeLineas=list()

def GanadorSegunMariano():
	ganador=["",0]
	for fila in listaDeLineas:
		while len(fila)!= 4:
			fila.append(0)
			print(fila)
	for corredor in listaDeLineas:
		puntos=0
		for posicion in corredor:
			if posicion==1:
				puntos=puntos+20
			if posicion==2:
				puntos=puntos+10
			if posicion==3:
				puntos=puntos+5
		if puntos>ganador[1]:
			ganador[0]=corredor[0]
			ganador[1]=puntos
	print("El ganador es: ",ganador)


def Existe(nombreCorredor,posicion):
	for fila in listaDeLineas:
		if fila[0]==nombreCorredor:
			fila.append(posicion)
			return False
	return True
		
		
def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:	
		for i in range(len(fila)):
			if fila[i]==" " and Existe(fila[0:i],int(fila[i+1:-1])):
				listaDeLineas.append([fila[0:i],int(fila[i+1:-1])])
				
for j in [1,2,3]:
	lecturaArchivos("a"+str(j)+".txt")

print(listaDeLineas)

GanadorSegunMariano()