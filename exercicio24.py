import os
os.system("cls")

n1 = int(input())
n2 = int(input())

def soma(n1, n2):
    soma = n1 +n2
    return soma

def subtracao(n1, n2):
    sub = n1 - n2
    return sub

def multiplicacao(n1, n2):
    multi = n1*n2
    return multi

def divisao(n1, n2):
    divisao = n1/n2
    return divisao


escolha = 1

while escolha:
    escolha = int(input("1 - Soma\n" +
          "2 - subtração\n" +
          "3 - Multiplicação\n" +
          "4 - Divisão\n" +
          "0 - Nenhuma\n"
          "Digite a sua escolha\n: "))
    if escolha ==1:
        print(soma(n1,n2))
    elif escolha ==2:
        print(subtracao(n1,n2))
    elif escolha ==3:
        print(multiplicacao(n1,n2))
    elif escolha == 4:
        print(divisao(n1,n2))




