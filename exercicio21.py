import os
os.system("cls")

numero = int(input("Digite o numero:"))

def inverter(numero):
    string = str(numero)
    return int(string[::-1])

print(inverter(numero))
