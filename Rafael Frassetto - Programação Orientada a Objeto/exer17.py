'''17) Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um
aluno, calcule e imprima a média (simples) desse aluno. Só devem ser
aceitos valores válidos durante a leitura (0 a 10) para cada nota.'''


a = float(input("nota 1:"))
b = float(input("nota 2:"))

while(a<0 or a>10):
    a = float(input("nota 1:"))
while(b<0 or b>10):
    b = float(input("nota 2:"))
z =(a*b)/2
print("media :{}".format(z))