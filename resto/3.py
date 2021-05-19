def aleatorio(numero):
	if numero == 4:
		file = open("a4.txt", "r")
		return(file.read())
	else:
		file = open("a" + str(numero) + ".txt" , "r")
		return(file.read())
			

while True:
	a = int(input("cual quieres: "))
	print(aleatorio(a))
	if aleatorio(a) == "no":
		continue		
	else: 
		break