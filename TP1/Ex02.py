def ordenar(lista):
    i = 0
    while i < 13:
        selecionado = lista[i]
        for j in range(i+1, 13):
            if selecionado < lista[j]:
                break
            else:
                lista.pop(i)
                lista.insert(j, selecionado)
                i = -1 #reinicia
                break
        i = i + 1
    return lista


cartas = [9, 11, 2, 8, 6, 1, 7, 13, 3, 5, 4, 10, 12]
print(cartas)
print(ordenar(cartas))