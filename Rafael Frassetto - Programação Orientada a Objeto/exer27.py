'''27) Uma empresa quer verificar se um empregado está qualificado para a
aposentadoria ou não. Para
estar em condições, um dos seguintes requisitos deve ser satisfeito:
- Ter no mínimo 65 anos de idade.
- Ter trabalhado no mínimo 30 anos.
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um algoritmo que leia: o número
do empregado (código), o ano
de seu nascimento e o ano de seu ingresso na empresa. O programa
deverá escrever a idade e o tempo
de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou
'Não requerer'.'''


codi = int(input("código: "))
nasci = int(input("ano de nascimento: "))
ingres = int(input("ano de ingresso na empresa: "))

ida = 2022-nasci
traba = 2022-ingres

if ida>=65:
    print("Idade:",ida,"\nTrabalho:",traba,"\nRequer aposentadoria.")
elif traba>=30:
    print("Idade:",ida,"\nTrabalho:",traba,"\nRequer aposentadoria.")
elif ida>=60 and ida<65 and traba>=25:
    print("Idade:",ida,"\nTrabalho:",traba,"\nRequer aposentadoria.")
else:
    print("Não requerer aposentadoria.")