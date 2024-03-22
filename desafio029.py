"""escreva um programa que leia a velocidade de um carro.

se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

a multa vai custar R$7,00 por cada km acima do limite. """

velocidade =int(input("A quantos km/h o carro está ? "))
ultrapassou = velocidade - 80
multa = ultrapassou * 7
if velocidade > 80 :
    print(f"Você foi multado e deverá pagar R$7,00 por cada km acima da velocidade permitida (80km/h). \nVocê estava a {velocidade}km/h, isso é {ultrapassou}km/h além do permitido, sendo assim, você deverá pagar uma multa no valor de {multa} reais")
else : 
    print("Você está dentro do limite de velocidade, nesse caso, não será multado.")    


 
