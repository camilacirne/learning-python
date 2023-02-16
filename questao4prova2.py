import os
os.system("cls")

frase = input("Digite a frase: ")
palavraSubstituida = ""
primeiraPalavra = ""

listaDePalavras = frase.split()
print(len(listaDePalavras))
i = 0

for lista in listaDePalavras:
    if i == len(listaDePalavras) - 1:
        palavraSubstituida = lista
    if i == 0:
        primeiraPalavra = lista
    i = i + 1 


print(frase.replace(lista,"fim"))
frase = (primeiraPalavra + " " + palavraSubstituida)
print(frase)