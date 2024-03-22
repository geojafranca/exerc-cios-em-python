"""
faça um programa que leia uma frase pelo teclado e mostre : 

quantas vezes aparece a letra 'A'. 

em que posição ela aparece a primeira vez.

em que posição ela aparece a última vez. 

"""

frase=str(input("Digite uma frase : ").lower())
frase2=frase.count("a")
pri=frase.find("a")
ult=frase.rfind("a")
print(f"A letra 'a' aparece {frase2} vezes na frase. \nA letra 'a' aparece pela primeira vez na posição {pri} e aparece a última vez na posição {ult} ")
