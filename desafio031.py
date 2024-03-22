"""desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens de mais longas"""

dist=int(input("Digite quantos km vamos percorrer nessa viagem : "))
if dist <= 200 :
    print(f"Ok, para uma viagem de {dist}km você deverá pagar {dist*0.50} reais")
else : 
    print(f"Ok, para uma viagem de {dist}km você deverá pagar {dist*0.45} reais")    