'''9) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma
empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total
das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor,
calcular e escrever o seu salário total.'''



salario = float(input("Digite o salário fixo :"))
comissao = float(input(" vendas do mes  :"))


if comissao<=1500:
    x = salario*1.03
    print("salario {}".format(x))
else:
    x = salario*1.05
    print("salario {}".format(x))
