notas = []
k = 1
while k <= 4: #contador comum
    notas.append(float(input("Nota: ")))
    k += 1

soma = k = 0

while k <= 3: #contador para acessar as notas da array
    soma = soma + notas[k]
    k += 1

print(f"Média {notas} é {soma/4:.1f}")
