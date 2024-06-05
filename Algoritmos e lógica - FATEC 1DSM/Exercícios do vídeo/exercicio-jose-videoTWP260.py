José = "entrou 6h" #var global

def fatec():
    global José #para dizer que o José será o mesmo
    José = "entrou 8h" #var local
    print(José)

print(José)
fatec()
print(José)
