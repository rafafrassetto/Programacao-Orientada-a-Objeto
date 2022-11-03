'''10) Faça um algoritmo para ler: número da conta do cliente, saldo, débito
e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo -
débito + crédito). Também testar se saldo atual for maior ou igual a zero
escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo
Negativo'.'''


conta = float(input("numero conta :"))
saldo = float(input("numero saldo :"))
debito = float(input("numero debito :"))
credito = float(input("numero credito :"))

saldoatual = saldo - debito + credito
print("Saldo atual : {}".format(saldoatual))

if saldoatual >=0:
    print("Saldo positivo")
else:
    print("Saldo negativo")