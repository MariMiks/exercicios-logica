#3)Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calculeo total em segundos
dia = int(input("Digite o dia de hoje: "))
h, m, s = input("Digite horas:minutos:segundos ").split(":")
h = int(h)
m = int (m) 
s = int(s)
total = dia*24*360 + h*360 + m*60 + s
print(f"Total em segundos: {total}")
