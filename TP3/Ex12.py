def soma(lista):
    n = len(lista)
    if n == 0:
        return 0
    return lista[n-1] + soma(lista[:n-1])

lista = [1, 2, 3, 3, 2, 1]
print(soma(lista))