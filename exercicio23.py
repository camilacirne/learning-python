import os
import random
os.system("cls")

numeros = []

def sorteia(numeros):
    for i in range(5):
        numeros.append(random.randint(0, 99))
    return numeros

def somaPar(numeros):
    soma = 0
    for i in range(len(numeros)):
        print(numeros[i])
        if numeros[i] % 2 == 0:
            soma = soma + numeros[i]
    return soma

numeros = sorteia(numeros)
print(somaPar(numeros))

