"""faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidadee de tinta para pinta-la. sabendo que cada litro de tinta pinta uma área de 2m²"""

largura=float(input("digite a largura da parede de sua casa (em metros) : "))
altura=float(input("digite a altura da parede de sua casa (em metros) : "))
area = largura*altura
ltinta = area/2
print(f"para pintar a parede de {area}m² toda, você irá precisar de {ltinta} litros de tinta.")