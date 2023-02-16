import os
os.system("cls")

nome = input("Digite o nome: ")

for i in range(len(nome) + 1):
    print(nome[:i])