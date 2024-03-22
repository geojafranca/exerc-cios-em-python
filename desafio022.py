"""crie um programa que leia o nome completo de uma pessoa e mostre : 
o nome com todas as letras maiúsculas.
o nome com todas as letras minúsculas.
quantas letras ao todo (sem os espaços).
quantas letras tem o primeiro nome."""

nome=str(input("digite seu nome completo : "))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ","")))
print(len(nome.split()[0]))