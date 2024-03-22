# as organizações tabajara resolveram dar um aumento de salario para seus colaboradores e lhe contrataram para desenvolver um programa que calculará os reajustes
# faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual :
# salários de até 280 : aumento de 20%
# salários entre 280 e 700 : aumento de 15%
# salários entre 700 e 1500 : aumento de 10%
# salários de 1500 em diante : aumento de 5%
# após o aumento ser realizado informe na tela : 
# o salário antes do reajuste; 
# o percentual do aumento aplicado;
# o valor do aumento;
# o novo salário após o reajuste.

slrI=float(input("Digite seu salário atual : "))
if slrI <=280 : 
    print(f"Seu salário atual é de : R$ {slrI}\nSeu percentual de aumento é de 20%, logo, seu salário teve um aumento de R$ {slrI*0.20}\nOu seja, seu novo salário é de R$ {slrI+(slrI*0.20)} ")
elif slrI > 280 and slrI <= 700 :
    print(f"Seu salário atual é de : R$ {slrI}\nSeu percentual de aumento é de 15%, logo, seu salário teve um aumento de R$ {slrI*0.15}\nOu seja, seu novo salário é de R$ {slrI+(slrI*0.15)} ")
elif slrI > 700 and slrI <= 1500 : 
    print(f"Seu salário atual é de : R$ {slrI}\nSeu percentual de aumento é de 10%, logo, seu salário teve um aumento de R$ {slrI*0.10}\nOu seja, seu novo salário é de R$ {slrI+(slrI*0.10)} ")
else :
    print(f"Seu salário atual é de : R$ {slrI}\nSeu percentual de aumento é de 5%, logo, seu salário teve um aumento de R$ {slrI*0.05}\nOu seja, seu novo salário é de R$ {slrI+(slrI*0.05)} ")
         