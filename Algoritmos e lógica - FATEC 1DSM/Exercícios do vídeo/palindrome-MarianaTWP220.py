#verificar se a palavra é palíndrome ou não
#palíndrome = escreve igual de trás para frente

texto = str(input("Palavra: "))

if texto[::-1] == texto:
    print("É um palíndrome")

else:
    print("Não é palíndrome")
