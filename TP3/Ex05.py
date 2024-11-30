def quick_sort(lista):
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
    return quick_sort(sublista1) + sublista2 + quick_sort(sublista3)

lista = [9, 1, 1, 9, 4, 7, 9, 5, 2, 4, 1, 6, 2, 5, 0]
print(quick_sort(lista))