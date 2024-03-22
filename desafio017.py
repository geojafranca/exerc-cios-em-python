"""faça um programa que leia o comprimento do cateto oposto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa"""

from math import sqrt, pow
cop=float(input("digite o comprimento do cateto oposto do triângulo retângulo : "))
cad=float(input("digite o comprimento do cateto adjacente do triângulo retângulo : "))
soma=pow(cop,2) + pow (cad,2)
raiz=sqrt(soma)
print(f"a soma do c oposto e do c adjacente é {soma} o comprimento da hipotenusa é {raiz}")