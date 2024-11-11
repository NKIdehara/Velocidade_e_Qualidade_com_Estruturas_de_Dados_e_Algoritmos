def inverte_fila(lista):
    aux = []
    while len(lista) > 0:
        aux.append(lista.pop())
    return aux

lista = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]
print(inverte_fila(lista))