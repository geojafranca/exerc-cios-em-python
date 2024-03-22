"""faça um programa que leia o nome completo de uma pessoa e mostre separadamente o primeiro e o último"""

nome=str(input("Digite seu nome completo : "))
nome2=nome.split()
print(f"Seu primeiro nome é : {nome2[0]} \nSeu último nome é : {nome2[-1]}")
