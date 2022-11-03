'''24) Um posto está vendendo combustíveis com a seguinte tabela de
descontos:
Escreva um algoritmo que leia o número de litros vendidos e o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90'''


l = float(input("litros que vc quer abastecer: "))
c = input("Digite A para álcool ou G para gasolina: ")
preco = 0
if c == "A" or c == "a":
    preco = l * 2.9
    if l <= 20:
        preco -= 2.9 * l * 3 / 100
    else:
        preco -= 2.9 * l * 5 / 100
elif c == "G" or c == "g":
    preco = l * 3.3
    if l <= 20:
        preco -= 3.3 * l * 4 / 100
    else:
        preco -= 3.3 * l * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")
