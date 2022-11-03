'''14) Ler dois valores e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.'''



a= float(input("Valor 1:"))
b = float(input("Valor 2:"))

if a == b:
    print("Números iguais")
elif a > b:
    print("Primeiro é maior")
else:
    print("Segundo maior")