'''18) Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do
exercício [17]. Se for respondido 'S' deve retornar e executar um novo
cálculo, caso contrário deverá encerrar o algoritmo.'''


a = float(input("nota 1:"))
b = float(input("nota 2:"))

while(a<0 or a>10):
    a = float(input("nota 1:"))
while(b<0 or b>10):
    b = float(input("nota 2:"))
c = input("")
z =(a*b)/2
print("media :{}".format(z))
d = input("NOVO CÁLCULO (S/N)?")
while (d =="s"):
    a = int(input("Um número"))
    b = int(input("Um número"))
else:
    print("Obrigado")