# tabuada simples usando while

s=0
n1=int(input("digite um número para que possa ver a tabuada : "))
while s < 10 :
    s+=1
    resultado = n1*s   
    print (f"{n1} X {s} = {resultado}")