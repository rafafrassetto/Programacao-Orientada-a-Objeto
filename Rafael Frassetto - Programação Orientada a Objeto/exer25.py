'''25) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
(considere que as idades dos homens serão sempre diferentes entre si,
bem como as das mulheres). Calcule e escreva a soma das idades do
homem mais velho com a mulher mais nova, e o produto das idades do
homem mais novo com a mulher mais velha.'''

home1 = float(input("Idade homem: "))
home2 = float(input("Idade homem:"))
m1 = float(input("Idade mulher: "))
m2 = float(input("Idade mulher: "))


if home1>home2 and m1<m2:
     print("Soma: ",home1+m1)

if home1<home2 and m1<m2:
     print("Soma: ",home2+m1)

if home1>home2 and m1>m2:
     print("Soma: ",home1+m2)

if home1<home2 and m1>m2:
     print("Soma: ",home2+m2)


if home1<home2 and m1>m2:
     print("Produto: ",home1*m1)

if home1>home2 and m1>m2:
     print("Produto: ",home2*m1)

if home1<home2 and m1<m2:
     print("Produto: ",home1*m2)

if home1>home2 and m1<m2:
     print("Produto: ",home2*m2)