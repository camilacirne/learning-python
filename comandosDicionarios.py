import os

os.system("cls")

#como declarar um dicionário
agenda = {}
agenda2 = dict()

# como inicializar
agenda = {"Pedro": 98734213} #Pode ser valores
agenda2 = { 'Maria': [9546789, 98765049],
            'Pedro': [98765432],
            'Joaquim': [987654326]} #Pode ser com uma lista
agenda3 = {
    "cpf1" : [input("Nome: "), int(input("Idade: ")), int(input("Telefone: "))],
    "cpf2" : [input("Nome: "), int(input("Idade: ")), int(input("telefone:"))]
}

#Para acessar os itens do dicionário tem que ser pela chave
print(agenda["Pedro"])

#for cpf in agenda3:
 #   print(f"{cpf}: {agenda3[cpf]}")


agenda.get("Ana", "Não encontrado") #Para acessar o item
agenda["Pedro"] = 8976540 #Para alterar o valor do conteúdo

print(agenda)

agenda.update(agenda2) #Comando utilizado para atualizar os dados do dicionário, se houver
#keys idênticas no momento do comando os values serão alterados, se
#a(s) key(s) forem diferentes, os dados serão adicionados ao dicionário.

#Para acrescentar novos valores no Dicionário
agenda["Teresa"] = 6758493

del agenda["Pedro"] #Para remover os valores do dicionário
print(agenda)

agenda2.pop("Maria", "não encontrado") #remove o elemento com a chave e retorna o valor

print(len(agenda)) #retorna o número de itens (chave e valores)

print("Joaquim" in agenda2) #verifica item no dicionário retorna true e false
print("87954433" in agenda) 
print([87934433] in agenda2.values()) #se for lista coloca[]

agenda.clear() #Remove todos os elementos do dicionario
agenda = {} #Remove todos os elementos do dicionario

print(agenda2.items()) #Retorna uma lista com todos os itens do dicionário

print(agenda2.keys()) #retorna uma lista com as chaves

print(agenda2.values()) #retorna uma list com os valores

for contato in agenda2:
    media = sum(agenda2[contato])/len(agenda2[contato])
    #print(media)
