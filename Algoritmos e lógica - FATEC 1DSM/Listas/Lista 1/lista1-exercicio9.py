#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro
#alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
#alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
#e R$ 0,15 por km rodado.

kmCarro = float(input("Quantidade percorrida pelo carro (km): "))
diaCarro = int(input("Quantidade de dias alugado: "))
total = kmCarro*0.15 + diaCarro*60
print(f"O preço a pagar do carro alugado será de R${total:.2f}")
