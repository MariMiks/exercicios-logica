a = 80000
b = 200000
taxaA = 3/100
taxaB = 1.5/100

n = 0

while a < b:
    aumentoA = a * taxaA
    aumentoB = b * taxaB

    a += aumentoA
    b += aumentoB
    n += 1

print(f"leva {n} anos para A ser maior que B")
     
 
