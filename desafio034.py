"""escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. 
   para salários superiores a R$ 1.250.00 calcule um aumento de 10%.
   para inferiores ou iguais, o aumento é de 15%"""

s=float(input("Olá, caro trabalhador, digite seu salário : "))
if s > 1250 : 
    aumento = s * 0.10
    print(f"Seu salário é equivalente a R${s}, nesse caso, você receberá um aumento de 10% \nSeu novo salário é {s+aumento}")
else : 
    aumento = s*0.15
    print(f"Seu salário é equivalente a R${s}, nesse caso, você recebera um aumento de 15% \nSeu novo salário é {s+aumento}")    