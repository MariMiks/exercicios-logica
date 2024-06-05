a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))

#triangulo = |a - b| < c < a + b

if abs(a - b) < c < a + b:
    print("é um triângulo")

else:
    print("Não é um triângulo")

if a == b == c:
        print("equilátero")

elif a == b or a == c or b == c:
        print("isósceles")

else:
#elif a != b or a != c or b != c:
    print("escaleno")


