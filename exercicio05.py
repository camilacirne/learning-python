import os
os.system("cls")

numeros = [3.5, 6.7, 1.0, 4.9]

numeros.insert(1, 2.3)

numeros.pop()

numeros[2] = 9.2

numeros.sort()

print(len(numeros))

print(numeros)

for c,v in enumerate(numeros):
    print(c,v, end =" ")