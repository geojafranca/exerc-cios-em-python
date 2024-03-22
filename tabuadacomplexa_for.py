#tabuada mais complexa, onde o usuário escolhe até que número a tabuada vai

n1=int(input("Digite o número que você deseja ler a tabuada : "))
m=int(input("Digite até que número sua tabuada vai : "))
for c in range (1,m) :
    resultado = n1*c
    print (f"{n1} X {c} = {resultado}")