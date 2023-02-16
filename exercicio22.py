import os
os.system("cls")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota2: "))

def media(nota1,nota2):
    soma = nota1 + nota2
    media = soma/2
    return media

def conceito(media):
    if media >= 6:
        return "aprovado"
    elif media < 6 or media >=4:
        return "verificação suplementar"
    else:
        return "reprovado"
    
media = media(nota1, nota2)
print(conceito(media))