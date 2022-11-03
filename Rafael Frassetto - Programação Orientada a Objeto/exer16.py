'''16) Escreva um algoritmo para ler 2 valores e se o segundo valor
informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo '''



a= float(input("Valor 1:"))
b = float(input("Valor 2:"))

while(b==0):
    b = int(input("digite valor:"))
c = a/b
print("Multiplicaçao :{}".format(c))