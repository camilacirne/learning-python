from datetime import date
import os 
os.system("cls")

quant = 0
quantMenor = 0
anoAtual = date.today().year

for i in range(5):
    anoDeNascimento = int(input("Escreve seu ano de nascimento: "))

    if (anoAtual - anoDeNascimento) >=18:
        quant = quant + 1
    else:
        quantMenor = quantMenor + 1

print( quantMenor, quant)
