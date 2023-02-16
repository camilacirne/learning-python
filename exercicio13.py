import os
os.system("cls")

estagiarios = [[],[],[]]
totalVT = 0.0
somaSalarios = 0.0

for estagiario in range(3):
    for dados in range(3):
        if dados == 0:
            print("Digite o salário: ")
        if dados == 1:
            print("Digite o vale-tranporte: ")
        if dados == 2:
            print("Digite o vale-alimentação:")
        estagiarios[estagiario].append(float(input()))
        
for estagiario in range(3):
    totalVT = totalVT + estagiarios[estagiario][1]
    somaSalarios = somaSalarios + estagiarios[estagiario][0]
    
print(estagiarios)
print(round(somaSalarios/3, 2), totalVT)