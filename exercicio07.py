import os
os.system("cls")

numeros = []

for i in range(10):
    numeros.append(int(input("Digite o numero inteiro:")))

print(numeros)
print(min(numeros))
print(max(numeros))

for numero in numeros:
    if numero % 2 != 0:
        print(numero)