a = int(input("Insira o primeiro número inteiro: "))
b = int(input("Insira o segundo número inteiro: "))

while a % b != 0:
    a, b = b, a % b

print(f"O máximo divisor comum entre os dois é {b} ")
