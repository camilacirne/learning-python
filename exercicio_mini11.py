import os
os.system("cls")

nome = input("Digite o nome: ").upper()
for i in range(len(nome)):
    print(nome[0:i+1])