var_juan = 0
var_fran = 0
var_gonzalo = 0
			

def ganador(s):
	a = open(s, "r").read()
	for i in range(len(a)):
		if a[i] == " " and a[i+1] == "1" and a[i-len("Juan")] == "J":
			return("Ha ganado Juan")
		elif a[i] == " " and a[i+1] == "1" and a[i-len("Gonzalo")] == "G":
			return("Ha ganado Gonzalo")
		elif a[i] == " " and a[i+1] == "1" and a[i-len("Fran")] == "F":
			return("Ha ganado Fran")


print(ganador("a1.txt"))
print(ganador("a2.txt"))
print(ganador("a3.txt"))


l = [ganador("a1.txt") , ganador("a2.txt") , ganador("a3.txt")]


for i in l:
	if i == "Ha ganado Juan":
		var_juan = var_juan + 1
	elif i == "Ha ganado Gonzalo":
		var_gonzalo = var_gonzalo + 1
	elif i == "Ha ganado Fran":
		var_fran == var_fran + 1


if var_juan >= 2:
	print("Juan ha ganado mas veces")
elif var_gonzalo >= 2:
	print("Gonzalo ha ganado mas veces")
elif var_fran >= 2:
	print("Fran ha ganado mas veces")

