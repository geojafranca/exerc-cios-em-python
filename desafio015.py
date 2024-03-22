"""crie um programa que leia a raiz quadrada de um número e arredonde ela para o número inteiro de baixo 
ex: 5.123
o número é 5
use a função from math import"""

from math import sqrt,floor
n1=int(input("digite um número : "))
raiz= sqrt (n1)
print(f"a raiz quadrada de {n1} é {floor (raiz)}")