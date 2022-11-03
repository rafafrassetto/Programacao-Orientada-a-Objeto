'''2) Escreva um algoritmo para ler o número total de eleitores de um
município, o número de votos brancos, nulos e válidos. Calcular e escrever
o percentual que cada um representa em relação ao total de eleitores. '''

eleitor = float(input("total de eleitores :"))
branco = float(input("total de votos brancos :"))
nulo = float(input("total de votos nulos :"))
validos = float(input("total de votos validos :"))

a = (eleitor/branco)*100
b = (eleitor/nulo)*100
c = (eleitor/validos)*100

print("branco :{}".format(a))
print("nulo :{}".format(b))
print("valido :{}".format(c))

