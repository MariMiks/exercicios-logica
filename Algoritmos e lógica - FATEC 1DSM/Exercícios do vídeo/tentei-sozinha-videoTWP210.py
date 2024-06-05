#O sistema lê 4 notas, e no final é impresso a lista completa
# e a média de todas elas

notas = []
soma = k = 0

while k <= 3:
    notas.append(float(input("Nota: ")))
    soma += notas[k]
    k += 1

media = soma/len(notas)
print(f"Média de {notas} = {media}")
