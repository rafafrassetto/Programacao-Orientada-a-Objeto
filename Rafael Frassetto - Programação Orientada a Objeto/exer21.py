'''21) Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.'''

cont=0
for i in range (1,11):
    num = int(input("Digite número: "))
    if (num<0):
        cont = cont + 1
print (cont)