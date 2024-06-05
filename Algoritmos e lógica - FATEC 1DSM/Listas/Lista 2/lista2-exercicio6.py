hora = float(input("Quanto ganha por hora: "))
horaMes = float(input("Horas trabalhadas no mês: "))

salarioBruto = hora * horaMes
IR = salarioBruto * 11/100
INSS = salarioBruto * 8/100
sindicato = salarioBruto * 5/100

salarioLiq = salarioBruto - IR - INSS - sindicato

print(f"Seu salário líquido é: R${salarioLiq:.2f}, com os descontos:")
print(f"Imposto de renda: R${IR:.2f}")
print(f"INSS: R${INSS:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
