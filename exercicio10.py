import os
os.system("cls")

matriz = [[],[],[]]
soma = 0.0

for aluno in range(3):
    for notas in range(4):
        matriz[aluno].append(float(input()))
        soma = soma + matriz[aluno][notas]  


print(round(soma/len(matriz),2)) #round para arrendondar as casa decimais


    