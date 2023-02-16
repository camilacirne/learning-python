import random
#from random import randint
import os
os.system("cls")

numeros = []

for i in range(5):
    numeros.append(random.randint(1,100))

tupla = tuple(numeros)
print(tupla, min(tupla), max(tupla))


#Tuplas podem conter objetos mutavéis como listas
numerosList = ([1,2,3],['a','b','c'])

print(numerosList[0])
print(numerosList[1])