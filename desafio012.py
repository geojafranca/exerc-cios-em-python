"""faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""

preco=float(input("digite o preço do produto para que possa receber seu desconto : R$ "))
novopreco=float(preco * 0.95)
print(f"o seu produto custava R$ {preco}, agora, com 5% de desconto, ele custa R$ {novopreco}")