"""faça um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem : 

o primeiro valor é maior
o segundo valor é menor
não existe valor maior, os dois são iguais """

n1=int(input("Digite o primeiro número inteiro : "))
n2=int(input("Digite o segundo número inteiro : "))
if n1 > n2 :
    print("O primeiro valor é maior")
elif n2 > n1 :
    print("O segundo valor é maior")
else :
    print("Não existe valor maior, os dois são iguais")        