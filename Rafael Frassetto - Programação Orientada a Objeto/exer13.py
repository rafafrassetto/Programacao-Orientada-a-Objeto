'''13) Ler 3 valores (considere que não serão informados valores iguais) e
escrever a soma dos 2 maiores'''

valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
valor3 = int(input("Digite valor 3: "))
if (valor3 < valor1) and (valor1 < valor2):
    print (valor1 + valor2)
elif (valor2 < valor1) and (valor1 < valor3):
    print (valor1 + valor3)
else:
    print (valor2 + valor3)

