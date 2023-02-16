import os
os.system("cls")

listaDealunos = { "Ana" : 8.8,
                  "Carol" : 9.1,
                  "Daniel" : 4.5 }
continuar = 1

while continuar:
    continuar = int(input("Escolha uma opção: \n" +
                          "0 - Sair \n" + 
                          "1 - Exibir lista de alunos com suas notas (cada aluno tem uma nota) \n" +
                          "2 - Inserir aluno e nota \n" +
                          "3 - Alterar a nota de um aluno \n" +
                          "4 - Consultar nota de um aluno específico \n" +
                          "5 - Apagar um aluno da lista \n"
                          "6 - Média \n" ))
    if continuar == 1:
        #print(listaDealunos.items())
        for nome in listaDealunos.keys():
            print(nome, listaDealunos[nome])
    elif continuar == 2:
        nome = input("Digite o nome do aluno :")
        nota = float(input(f"Digite a nota de {nome}: "))
        listaDealunos[f"{nome}"] = nota 
    elif continuar == 3:
        print("Alunos: ", listaDealunos.keys())
        nome = input("Digite o nome do aluno que você quer alterar a nota: ")
        nota = input("Digite a nova nota: ")
        listaDealunos.get(f"{nome}", "não encontrado")
        listaDealunos[f"{nome}"] = nota 
    elif continuar == 4:
        nome = input("Digite o nome do aluno: ")
        print(listaDealunos.get(f"{nome}", "não encontrado"))
    elif continuar == 5:
        nome = input("Digite o nome do aluno: ")
        del listaDealunos[f"{nome}"] 
        #listaDealuno.pop(nome)
    elif continuar == 6:
        soma = 0
        for count in listaDealunos.values():
            soma = soma + count
        print("%.2f" % (soma/len(listaDealunos)))
    else:      
        print("invalido")
    