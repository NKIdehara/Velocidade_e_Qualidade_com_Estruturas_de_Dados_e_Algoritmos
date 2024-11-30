def quick_select(lista, posicao):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    sublista1 = []
    for i in lista:
        if i < pivo:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i == pivo:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i > pivo:
            sublista3.append(i)

    if posicao < len(sublista1):
        return quick_select(sublista1, posicao)
    elif posicao < len(sublista1) + len(sublista2):
        return pivo
    else:
        return quick_select(sublista3, posicao - len(sublista1) - len(sublista2))

lista = [9, 1, 1, 9, 4, 7, 9, 5, 2, 4, 1, 6, 2, 5, 0]
posicao = 6
print(quick_select(lista, posicao))