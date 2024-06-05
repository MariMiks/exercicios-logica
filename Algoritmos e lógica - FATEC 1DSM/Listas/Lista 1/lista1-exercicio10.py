#10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o total de dias

cigarDia = int(input("Quantos cigarros vc fuma por dia? "))
anosFuma = int(input ("A quantos anos vc fuma? "))
totalCigar = anosFuma*365*cigarDia
diasPerdidos = totalCigar/144
print(f"Você já perdeu {diasPerdidos:.1f} dias da sua vida")
