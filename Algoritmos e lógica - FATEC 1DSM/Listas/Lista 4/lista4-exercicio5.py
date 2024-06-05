texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.lower()
texto = texto.split()

def python(texto):
    for k in texto:
        if k in "python":
            return True
    return False

lista = []

for n in texto:
    if python(n)and len(n) <= 4:
        lista.append(n)
print(lista)

    
