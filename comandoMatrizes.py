import os
os.system("cls")

matriz = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"Digite o valor para linha {linha} e coluna {coluna}: ")))


for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^3}]", end="") #:^3 é a quantidade de espaço dentro do colchetes
    print() #para pular as linhas
    