import os
os.system("cls")

vetorPerguntas =["Conhece a vítima do roubo?", "Esteve no local do roubo?", "Mora perto da vítima?","A vítima lhe devia?", "Já trabalhou com a vítima?"]
i= 0
vetorResposta = []

while i< len(vetorPerguntas):
    print(vetorPerguntas[i])
    print("1-S,2-N")
    vetorResposta.append(int(input()))
    i = i + 1


if vetorResposta[1] == 1:
    print("Suspeita")
elif vetorResposta[2] == 1 or vetorResposta[3] == 1:
    print("Cúmplice")
elif vetorResposta[4] == 1:
    print("Ladrão")
else:
    print("Inocente")
