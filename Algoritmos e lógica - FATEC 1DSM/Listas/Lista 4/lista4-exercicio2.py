import random

lista = random.sample(range(1, 101), 20)
par = []
impar = []

for n in lista:
    if n%2 != 0:
        impar.append(n)
    else:
        par.append(n)




print(lista)
print(f"Pares: {par}")
print(f"Ímpares: {impar}")
