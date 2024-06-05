def épar(x):
    return x%2 == 0

#código professor
def fat(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f

def fatorial(n):
    fat = 1
    k = 1
    while k <= n:
        fat = fat * k
        k = k + 1
    return fat

#return == permite a manipulação do conteúdo
#print == apenas imprime na tela
