"""faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade : 

se ele ainda vai se alistar ao serviço militar.

se é a sua hora de se alistar.

se já passou o tempo do alistamento. """

from datetime import date
ano=int(input("digite o ano do seu nascimento :"))
idade= date.today().year - ano 
if idade < 18 :
    print("Ainda não está na hora de você se alistar")
elif idade == 18 :
    print("Você precisa se alistar")
else :
    print("Já passou da hora de você se alistar")    
