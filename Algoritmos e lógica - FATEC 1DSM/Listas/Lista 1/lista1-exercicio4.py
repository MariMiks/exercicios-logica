#4) Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário

salarioInicial = int(input("Seu salário inicial: "))
porcentagem = int(input("Qual a porcentagem de aumento? "))
aumento = (porcentagem*salarioInicial)/100
novoSalario = aumento + salarioInicial
print(f"O seu aumento será de R${aumento} e seu novo salário será R${novoSalario}")
