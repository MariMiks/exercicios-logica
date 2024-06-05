#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

tempC = float(input("Temperatura em °C: "))
tempF = 9*tempC/5 + 32
print(f"A temperatura {tempC:.2f}°C convertida em Farenheit é {tempF:.2f}F")
