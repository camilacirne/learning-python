import os 
os.system("cls")
numeroInicial = int(input("Digite o número inicial do intervalo: "))
numeroFinal = int(input("Digite o número final do intervalo: "))
i = numeroInicial
j = numeroFinal
while i != j:
    
    if i % 2 == 0:
        print(i)
    if numeroFinal - numeroInicial >= 0:
        i = i + 1
        j = numeroFinal + 1
    if numeroFinal - numeroInicial < 0:
        i = i - 1
        j = numeroFinal - 1


