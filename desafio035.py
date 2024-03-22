"""desenvolva um programa que leia o comprimento de 3 retas e diga se ela pode ou não se tornar um triângulo"""

r1=float(input("Digite o comprimento da primeira reta : "))
r2=float(input("Digite o comprimento da segunda reta : "))
r3=float(input("Digite o comprimento da terceira reta : "))
if r1 > r2 and r1 > r3 :
    print(f"O maior número é {r1}")
    if r2 + r3 > r1:
        print("É possível formar um triângulo")  
    else :
        print("Não é possível formar um triângulo")  
elif r2 > r1 and r2 > r3 :
    print(f"O maior número é {r2}")
    if r1 + r3 > r2 : 
        print("É possível formar um triângulo")
    else :
        print("Não é possível formar um triângulo")
else : 
    print(f"O maior número é {r3}")
    if r1 + r2 > r3 :
        print("É possível formar um triângulo")      
    else :
        print("Não é possível formar um triângulo")                     