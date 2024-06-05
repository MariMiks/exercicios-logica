lista = []

for k in range(18644, 33088):
    if "2" in str(k) and not "7" in str(k):
        lista.append(k)

print(f"{len(lista)}")
