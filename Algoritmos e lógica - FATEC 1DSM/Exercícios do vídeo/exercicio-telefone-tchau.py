minutos = int(input("Minutos falados no telefone: "))

if minutos < 200:
    conta = minutos*0.2

elif minutos <= 400:
    conta = minutos*0.18

elif minutos <= 800:
    conta = minutos*0.15

#elif minutos > 800:
#   conta = minutos*0.08

else
    conta = mintuos*0.08

print (f"Sua conta telefônica ficou R${conta:.2f}")
