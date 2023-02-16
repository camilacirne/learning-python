import os
os.system("cls")

quantidadeDeVendas = int(input("Quantas vendas foi realizada hoje: "))

peso = []

for i in range(quantidadeDeVendas):
    peso.append(float(input(f"Para a venda {i+1}, diga o peso: ")))

pesoMedio = sum(peso)// len(peso)
print(pesoMedio)

print(max(peso), min(peso))

print((sum(peso) * 4.35) )
