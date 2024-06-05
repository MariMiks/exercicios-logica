# 1 1 2 3 5 8 13 21 34 55...

f1, f2 = 1, 1
posicao = int(input("Até onde você quer que vá: "))
n = 0

print(f1)
posicao -= 1

while posicao > n:
    f1, f2 = f2, f1 + f2
    print(f1)
    n += 1

print(f"F{posicao+1} = {f1}")
