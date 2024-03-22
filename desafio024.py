"""crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo" """

cidade=str(input("digite o nome da cidade : ").strip())
cidade2="Santo" in cidade.capitalize()
print(f"sua cidade começa com o nome Santo ? \n {cidade2}")