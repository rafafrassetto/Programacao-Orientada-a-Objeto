'''5) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a
média final deste aluno. Considerar que a média é ponderada e que o
peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:'''


nota1 = float(input("Primeira Nota :"))
nota2 = float(input("Segunda Nota :"))
nota3 = float(input("Terceira Nota :"))

media = (nota1*2) + (nota2*3) + (nota3*5)/10
print(media)