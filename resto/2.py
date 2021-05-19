file = open("archivo.txt" , "r")
b = len("<!DOCTYPE html>")
a = file.read(b)
print(a)
if a == "<!DOCTYPE html>" or a == "<!doctype html>" :
	print("Es un HTML")
else:
	print("No es un HTML")