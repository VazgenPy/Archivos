#Python password generator
import random


lower = "qwertyuiopasdfghjklñzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"


todo = lower + upper + numbers + symbols
lenght = int(input("Cuantos caracteres quieres que tenga la contraseña (Maximo 77 caracteres): "))
password = "".join(random.sample(todo , lenght))
print(password)