'''8) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma
mensagem que diga se ela poderá ou não votar este ano (não é necessário
considerar o mês em que a pessoa nasceu).'''



ano = float(input("Digite o ano atual :"))
nascimento = float(input("Digite que vc nasceu :"))

a = ano - nascimento

if a >= 16:
    print("Pode Votar")
else:
    print("Nao pode votar")