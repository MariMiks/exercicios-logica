import random

lista1 = random.sample(range(1, 101), 10)
lista2 = random.sample(range(1, 101), 10) 
lista3 = []

for k in range(10):
    lista3.append(lista1[k])
    lista3.append(lista2[k])

print(lista1)
print(lista2)
print(lista3)
