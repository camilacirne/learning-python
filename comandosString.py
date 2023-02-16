import os

os.system("cls")

linda = "  Camila é linda"
camila = "camila camila é ok"

print(len(linda)) #Retorna o numero de caracteres
print(linda.find('mila')) #Retorna onde começa
print(linda.find('ana')) #Retona -1 se não tiver

print('Camila' in linda)

print(linda.upper())
print(linda.lower())
print(linda.capitalize()) #Muda a primeira letra da primeira palavra, para maiusuclo e minuscula
print(linda.title()) #Deixa maiusculo todo a primeira letra de todas as palavras
print(linda.replace("linda", "maravilhosa e linda"))
print(camila.replace("camila", "diva", 2)) #quantidade de trocas
print(camila.split()) #separa tudo em uma lista

#remove os caracteres do começo e do final da string.
print(linda.strip())

#remove apenas do começo da string
print(camila.lstrip("camila "))

#remove apenas do final da string
print(camila.rstrip("ok"))

lista = ["La", "mansion", "de", "los", "Hidalgo"]

print(" ".join(lista))

#Repetição de string
print(linda*3)

#substring ou fatiação de string
print(linda[3:9])

#inversão de string
print(linda[::-1])
