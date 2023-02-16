import os
os.system("cls")

dicionario2 = {}


dicionario = {
    input("Digite o nome do grupo 1: ") : [[]],
    input("Digite o nome do grupo 2: ") : [[]],
    input("Digite o nome do grupo 3: ") : [[]]
}

for grupo in dicionario:
    alturas = []
    altura = 0.0
    for i in range(3):
        altura = float(input(f"Digite a altura da pessoa {i+1} do {grupo}: "))
        alturas.append(altura)
        dicionario[f"{grupo}"] = alturas

print(dicionario)

for grupo in dicionario:
    media = (sum(dicionario[f"{grupo}"])/ len(dicionario[f"{grupo}"]))
    dicionario2[f"{grupo}"] = float("{:.2f}".format(media))

print(dicionario2)


medias = dicionario2.values()
print(medias)

for media in medias:
    maiorMedia = 0.0
    if media >= maiorMedia:
        maiorMedia = media

print(maiorMedia)
    


