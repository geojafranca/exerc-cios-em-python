"""crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
ex: digite um número : 6.127
o número 6.127 tem a parte inteira 6.  """

from math import trunc
nr1=float(input("digite um número real : "))
ni1=trunc(nr1)
print(f"o número real {nr1} tem a sua parte inteira {ni1} ")
