"""faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""

n1=(input("digite um número entre 0 e 9999 para que possa ver seus digitos separados : "))
milhar=(n1[-4])
centena=(n1[-3])
dezena=(n1[-2])
unidade=(n1[-1])
print(f"pois bem, aqui está : \n milhar : {milhar}000 \n centena : {centena}00 \n dezena : {dezena}0 \n unidade : {unidade} ")
