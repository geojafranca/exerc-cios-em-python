"""faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

ano=int(input("Digite o ano para saber se ele é bissexto : "))
if ano % 4 == 0 : 
    print(f"{ano} é um ano bissexto")
else :
    print(f"{ano} não é um ano bissexto")    
