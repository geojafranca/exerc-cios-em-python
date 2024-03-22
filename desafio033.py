"""faça um programa que leia 3 números e mostre qual é o maior e qual é o menor"""
n1=int(input("Digite 3 números : \n"))
n2=int(input())
n3=int(input())
if n1 > n2 > n3 : 
    print(f"O maior número é o {n1} e o menor é o {n3}")
elif n1 > n3 > n2 :
     print(f"O maior número é o {n1} e o menor é o {n2}")
elif n3 > n2 > n1 :
     print(f"O maior número é o {n3} e o menor é o {n1}")
elif n3 > n1 > n2 :
     print(f"O maior número é o {n3} e o menor é o {n2}")
elif n2 > n3 > n1 :
     print(f"O maior número é o {n2} e o menor é o {n1}")  
elif n2 > n1 > n3 :  
     print(f"O maior número é o {n2} e o menor é o {n3}")
else :
     print("opa, parece que você digitou números repetidos")             
 
   
        