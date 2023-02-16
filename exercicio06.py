import os
os.system("cls")

notas = []

for i in range(5):
    notas.append(int(input("Digite a nota do aluno: ")))


print(sum(notas))
print(sum(notas)/len(notas))

for nota in notas:
    if nota >= (sum(notas)/len(notas)):
        print(nota)
