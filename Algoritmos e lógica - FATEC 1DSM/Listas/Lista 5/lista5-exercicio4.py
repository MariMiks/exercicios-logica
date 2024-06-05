resposta = []

for val in range(1067, 3628):
    if val % 2 == 0 and val % 7 == 0:
        resposta.append(val)

print(f"São pares: {len(resposta)}")
        
