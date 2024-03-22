"""um professor quer sortear a ordem de apresentação dos tranalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""

import random
a1=str(input("digite o nome do primeiro aluno : "))
a2=str(input("digite o nome do segundo aluno : "))
a3=str(input("digite o nome do terceiro aluno : "))
a4=str(input("digite o nome do quarto aluno : "))
lista=(a1,a2,a3,a4)
ordem=random.sample(lista,4)
print(f"a ordem sorteada foi {ordem}")