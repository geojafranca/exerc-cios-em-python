"""crie um programa que faça o computador pensar em um número inteiro entre 5 e 0 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

o programa deverá escrever na tela se o usuário venceu ou perdeu"""

import random
n2=random.randint(0,5)
n1=int(input("o computador escolheu um número inteiro entre 0 e 5, qual número você acha que foi ? "))
if n1==n2 : 
    print("Parabéns, você acertou")
else : 
    print(f"poxa, infelizmente você errou, o computador pensou no número {n2}")    