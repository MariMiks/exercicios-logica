num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro é maior")

elif num2 > num1 and num2 > num3:
    print("O segundo é maior")

else:
    print("O terceiro é maior")
