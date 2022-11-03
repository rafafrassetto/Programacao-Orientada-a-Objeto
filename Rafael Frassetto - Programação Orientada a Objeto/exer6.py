'''6) As maçãs custam R$ 1,30 cada se forem compradas menos de uma
dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs compradas, calcule e escreva o
custo total da compra.'''


maca = float(input("Digite quantas Maças vc comprou :"))

if maca>=12:
    print(f'Total:R${maca}')
else:
    print(f'Total:R${maca*1.30}')

