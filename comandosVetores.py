

nomeDoVetor = [1,2]

novoValor = 5

indice = 0

nomeDoVetor[indice] = novoValor

nomeDoVetor.append(novoValor)

nomeDoVetor.sort()

nomeDoVetor.sort(reverse = True)

len(nomeDoVetor)

#Adicionar um novo valor em um indice especifico
nomeDoVetor.insert(indice, novoValor)

#Remove o último valor
nomeDoVetor.pop()

#Remove um valor de um indice específico
nomeDoVetor.pop(indice)

#Remove um valor pelo conteúdo
nomeDoVetor.remove(novoValor)


#Para deixar tudo na mesma linha
valores = [5,7,9]

for v in valores:
    print(f"{v}...", end =" ")

# enumare recebe a posição e os valores
for c,v in enumerate(valores):
    print(f"na posição {c}, tem o valor {v} ")

# print formato que é o f, permite imprimir o valor dentro de uma string

valores.index('5')
valores.count('5')

min(valores)
max(valores)
sum(valores)
