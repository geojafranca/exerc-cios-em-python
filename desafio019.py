"""um professor quer sortear um dos seus 4 alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido"""

import random
a1=str(input("digite o nome do primeiro aluno : "))
a2=str(input("digite o nome do segundo aluno : "))
a3=str(input("digite o nome do terceiro aluno : "))
a4=str(input("digite o nome do quarto aluno : "))
lista=(a1,a2,a3,a4)
aesc= random.choice (lista)
print(f"o aluno (a) escolhido para apagar o quadro foi {aesc}")