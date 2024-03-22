"""faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo"""

from math import sin, cos, tan, radians
n1=float(input("digite um ângulo em graus para que saiba o valor de seno, cosseno e tangente : "))
rad=radians(n1)
seno=sin(rad)
cose=cos(rad)
tang=tan(rad)
print(f"o valor de seno é {seno}, o de cosseno é {cose} e o da tangente é {tang}")
