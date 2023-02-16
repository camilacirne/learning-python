import os
os.system("cls")
alunos = []

arquivos = open("questao1.txt", "r")


for aluno in arquivos:
    alunos = aluno.split(" ")
    
    for i in range(1, len(alunos)-1):
        if int(alunos[i]) >= 6:
            nomedoaluno = alunos[0]



print(alunos)
print(nomedoaluno)
arquivos.close()
