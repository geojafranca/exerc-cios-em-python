"""crie um programa que peça um número inteiro qualquer e diga ao usuário para escolher qual será a base de conversão
1 para binário
2 para octal
3 para hexadecimal"""

n=int(input("Digite um número inteiro : "))
e=int(input("Digite o caracter que corresponde a base que você deseja converter esse número \n1-binário \n2-octal \n3-hexadecimal \n"))
if e == 1 : 
    print(bin(n))
elif e == 2 : 
    print(oct(n))
else : 
    print(hex(n))
        

