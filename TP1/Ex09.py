def bubbleSort(lista):
    i = 0
    while i < len(lista):
        selecionado = lista[i]
        for j in range(i, len(lista)-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                i = -1 #reinicia
                break
        i = i + 1
    return lista

lista = [9, 11, 2, 8, 6, 1, 7, 13, 3, 5, 4, 10, 12]
print(lista)
print(bubbleSort(lista))