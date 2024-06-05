area = float(input("Área (m²): "))

#1L --- 3m²
#18L --- x
#x = 18*3 = 54
#lata = 18L ---- R$80,00 ----- 54m²

if area % 54 > 0:
    latas = int(area/54) + 1
    print(f"Você irá precisar de {latas} latas")

else:
    latas = int(area/54)
    print(f"Você irá precisar de {latas} latas")

    
custo = latas * 80
print(f"Terá o custo de R${custo} com as latas")
