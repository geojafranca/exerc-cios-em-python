"crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome"

nome=str(input("Digite seu nome completo : ").strip())
nome2= "silva" in nome.lower()
print(f"Tem 'Silva' no seu nome ? {nome2}")