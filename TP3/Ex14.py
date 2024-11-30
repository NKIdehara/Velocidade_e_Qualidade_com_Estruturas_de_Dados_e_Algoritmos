def soma_lista(lista):
    n = len(lista)
    if n == 0:
        return 0
    return lista[n-1] + soma_lista(lista[:n-1])


print(soma_lista([1, 2, 3, 4]))