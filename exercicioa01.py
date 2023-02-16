import os
os.system("cls")

file = open("questao1.txt", "r")
soma = 0.0
qtd = 0
media = 0.0

for numero in file:
    soma = soma + float(numero) 
    qtd = qtd + 1

file.close()

media = soma/qtd
print(f"{media:.2f}")
