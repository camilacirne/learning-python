import os

os.system("cls")

valor = int(input("Digite um valor: "))

print("Valor em binário: {:b}".format(valor))
print(f"O número em binário é {valor:b}")
print("Valor na tabela ASCII: {0:c}".format(valor)) #Retorna o caracter na tabela ASCII
print("Valor em casa decimal: {:d}".format(valor))
print("Valor em octal: {:o}".format(valor))
print("Valor em hexadecimal: {:x}".format(valor))
print("Valor em hexadecimal: {:X}".format(valor))

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
print("O número no formato português é {:n}".format(valor))
print("\n\n")
numero = 15.907

print("Valor em notação cienfica: {:e}".format(numero))
print("Valor em notação cientifica com o separador E maiusculo: {:E}".format(numero))
print("Valor com 6 casas decimais após a virgula: {:f}".format(numero))
print("Valor com casas arredondadas após a virgula: {:.3f}".format(numero))
print("numero no formato regional: {:n}".format(numero))

print("\n")

print("Valor em %: {:%}".format(0.05))
print("Valor em % com 3 casas após a virgula: {:.3%}".format(0.05))
