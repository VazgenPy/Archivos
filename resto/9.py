archivo = open("a5.txt" , "w")
archivo.write(input("Escribe tu primera palabra: \n \t") + "\n")
archivo.close()

archivo = open("a5.txt" , "a")
archivo.write(input("Dime que quieres poner: \n \t") + "\n")
archivo.close()


