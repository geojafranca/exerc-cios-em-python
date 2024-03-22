"""faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento"""

salario=float(input("digite seu salário : R$ "))
aumento= 0.15 * salario
novosalario=salario+aumento
print(f"seu novo salário é : R$ {novosalario}")