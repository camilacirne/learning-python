import os
os.system("cls")

vetorA = []
vetorB = []

for i in range(5):
    vetorA.append(int(input()))
    vetorB.append(int(input()))

vetorC = vetorA + vetorB
somaPares = 0
somaImpares = 0
cont = 0
for numeros in vetorC:
    if numeros % 2 == 0:
        somaPares = somaPares + numeros
    else:
        somaImpares = somaImpares + numeros
        cont = cont + 1

print(somaPares, somaImpares/cont, min(vetorC))