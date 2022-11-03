'''26) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3
verificações e a média dos exercícios que fazem parte da avaliação.
Calcular a média de aproveitamento, usando a fórmula abaixo e escrever
o conceito do aluno de acordo com a tabela de conceitos mais abaixo:'''


n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

m = (n1+n2+n3)/3
ap = ((n1+(n2*2)+(n3*3))+m)

if ap >=9:
    print("Conceito: A")

if ap >=7.5 and ap<9:
    print("Conceito: B")

if ap >=6 and ap <7.5:
    print("Conceito: C")

if ap <6:
    print("Conceito: D")