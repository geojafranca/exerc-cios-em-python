# tabuda mais complexa, usando while

s=0
n1=int(input("Digite um número para que possa ver a tabuada : "))
m=int(input("Digite o número máximo que sua tabuada deve ir : "))
while s < m :
    s+=1
    resultado=n1*s
    print(f"{n1} X {s} = {resultado}")