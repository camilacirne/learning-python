import os
os.system("cls")
numero =[]

for i in range(5):
    num = (int(input()))
    if len(numero) == 0:
        n0 = num
        numero.append(n0)
    elif num < n0:
        numero.insert(0,num)
    else:
        numero.append(num)


print(numero)
          