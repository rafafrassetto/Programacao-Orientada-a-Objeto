'''7) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média
aritmética simples e escrever uma mensagem que diga se o aluno foi ou
não aprovado (considerar que nota igual ou maior que 6 o aluno é
aprovado). Escrever também a média calculada.'''

nota1 = float(input("Digite a Primeira Nota :"))
nota2 = float(input("Digite a Segunda Nota :"))
             
media = (nota1 + nota2)/2
             
if media >=6:
    print("Aprovado, com média {}".format(media))
else:
    print("Não Aprovado, com média {}".format(media))

