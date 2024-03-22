#faça um programa que leia um número e exiba o dia correspondente a da semana. (1-domingo, 2-segunda...)
#se digitar outro valor, deverá aparecer valor inválido.

n1=int(input("Digite um número entre 1 e 7 para que possa saber o dia da semana : "))
while n1 >= 8 :
    n1=int(input("valor inválido, só serão aceitos valores entre 1 e 7\nDigite novamente : "))
else :
    if n1 == 1 :
        print(f"o valor digitado foi {n1}, que corresponde a : domingo")
    elif n1 == 2 : 
        print(f"o valor digitado foi {n1}, que corresponde a : segunda-feira")
    elif n1 == 3 : 
        print(f"o valor digitado foi {n1}, que corresponde a : terça-feira")
    elif n1 == 4 : 
        print(f"o valor digitado foi {n1}, que corresponde a : quarta-feira")
    elif n1 == 5 : 
        print(f"o valor digitado foi {n1}, que corresponde a : quinta-feira")
    elif n1 == 6 : 
        print(f"o valor digitado foi {n1}, que corresponde a : sexta-feira")
    elif n1 == 7 : 
        print(f"o valor digitado foi {n1}, que corresponde a : sábado")