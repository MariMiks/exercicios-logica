velocidade = float(input("Velocidade km/h: "))

if velocidade > 110:
    multa = (velocidade-110)*5
    print(f"Você foi multado no valor de R${multa:.2f}")
else:
    print("Você está correto!")
