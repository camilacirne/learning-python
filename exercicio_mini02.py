import os
os.system("cls")

alturaMaxima = float(input())
alturaMinima = float(input())
quantidadeDeVisitantes = int(input())
alturaDeTodosOsVisitantes = []

for i in range(quantidadeDeVisitantes):
    alturaDeTodosOsVisitantes.append(float(input()))

podeIr = 0

for altura in alturaDeTodosOsVisitantes:
    if altura <= alturaMaxima and altura >=alturaMinima:
        podeIr = podeIr + 1

print(podeIr)