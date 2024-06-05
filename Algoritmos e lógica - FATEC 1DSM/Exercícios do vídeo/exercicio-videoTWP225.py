palavra = input("Palavra: ")
k = 0
troca = '' #acumulador
while k < len(palavra):
    if palavra[k] in "aeiou": #in == dentro deste produto
        troca = troca + "*"
    else:
        troca = troca + palavra[k]
    k = k + 1
print(troca)
