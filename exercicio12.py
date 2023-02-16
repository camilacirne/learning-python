import os
os.system("cls")

quantidadeDeRefrigerantes = [[],[],[],[]]

for trimestre in range(4):
    for regioes in range(5):
        quantidadeDeRefrigerantes[trimestre].append(int(input()))
        quantidadeTotal = quantidadeDeRefrigerantes[trimestre][regioes]

for trimestre in range(4):
    for regioes in range(5):
        print(f"{quantidadeDeRefrigerantes[trimestre][regioes]:^4}", end="")
    print()

print(quantidadeTotal)
