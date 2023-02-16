import os
os.system("cls")

matriz =[[],[],[]]
somaImpares = 0
soma = 0
menor = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input()))

for linha in range(3):
    soma = soma + matriz[linha][0]
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^3}]", end="")
        if matriz[linha][coluna] % 2 != 0:
            somaImpares = somaImpares + matriz[linha][coluna]
        menor = min(matriz[2])
    print()


print(soma, somaImpares, menor)