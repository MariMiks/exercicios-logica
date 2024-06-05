import calendar
ano = int(input("Ano: "))

if calendar.isleap(ano) == True:
   print(f"{ano} é um ano bissexto")

else:
    print(f"{ano} não é um ano bissexto")
