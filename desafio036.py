"""escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa vai perguntar o valor de uma casa, o salário do comprador e em quantos anos ele vai pagar

calcule o valor de prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado"""

vlc=float(input("Digite o valor da casa : "))
slc=float(input("Digite qual o seu salário : "))
qtn=int(input("Digite em quantos anos você quer pagar : "))
porc=slc*0.30
prest=int(vlc/(12*qtn))
if prest <= porc :
    print(f"Parabéns!!! seu empréstimo foi aceito, você deverá pagar R${prest} por mês durante {qtn*12} meses")
else :
    print("Poxa, infelizmente seu empréstimo foi negado")    
print("Obrigado por escolher nosso banco, volte sempre")    

