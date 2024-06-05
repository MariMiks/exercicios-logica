#5) Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

precoMercadoria = float(input("Valor da mercadoria: "))
percentual = int(input("Percentual de desconto: "))
desconto = (precoMercadoria*percentual)/100
novoPreco = precoMercadoria - desconto
print(f"O seu desconto será de R${desconto} e o novo valor a se pagar é de R${novoPreco}")
