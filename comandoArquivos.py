import os

os.system("cls")

file = open("arquivo.txt", "r")
dados = file.read() #passar os dados para um arquivo para eles não serem alterados
#file.write("Camila é linda")
#print("1",file.read())
#•writelines(): recebe um objeto iterável (seja uma lista, uma tupla, um dicionário, etc). 
# Com este método, várias linhas poderão ser inseridas no arquivo de uma vez.
print("2",file.readline())#retorna a primeira linha
print("3",file.readlines()) #retorna como uma lista

palavras = dados.split() #assim os dados viram uma lista, e eu posso manipular eles
print("Quantidade de caracteres: ", len(dados))
print("Quantidade de palavras: ", len(palavras))

file.close()

#modos

#"r" -> reading
#"w" -> write
#"a" -> open for writting in the end, acrescentar algo escrevendo, se não existir cria um arquivo vazio
#"b" -> binary mode
#"t" -> text mode
#"+" -> open for updating (reading or writing)
#"x" -> exclusive creation
# ai pode ser "r+, leitura e escrita", "w+", "r+b"

#pointer, é onde o arquivo vai ser adicionado, o a por exeplo o pinter está no final.

#se tentar ler mais de uma vez com read, ele vai pra ultima linha :(
# tell() retorna a posição do cursor em número de bytes
