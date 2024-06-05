peso = float(input("Peso do peixe (Kg): "))

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print(f"Você foi multado no valor de {multa}")

else:
    excesso = 0
    multa = 0
    print(f"Parabéns! O valor de excesso é {excesso}, e de multa {multa}")  
