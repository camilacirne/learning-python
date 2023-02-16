import os
os.system("cls")

matriz = [[],[],[]]
soma, somaB, somaC, somaA =[], 0.0,0.0,0.0

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(float(input()))
        
for linha in range(3): 
    
        somaB = somaB +(matriz[linha][0])
        somaA =somaA +(matriz[linha][1])
        somaC =somaC+(matriz[linha][2])

soma.append(somaB)
soma.append(somaA)
soma.append(somaC)
print(matriz, soma)