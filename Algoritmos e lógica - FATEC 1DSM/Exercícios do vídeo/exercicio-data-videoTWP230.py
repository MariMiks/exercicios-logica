d, m, a = input("dd/mm/aaaa: ").split("/")
meses = '''janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro'''.split()

posicaoM = int(m) - 1
print(f"{d} de {meses[posicaoM]} de {a}")

#print(f"{d} de {meses[int(m)-1]} de {a}") código do prof
