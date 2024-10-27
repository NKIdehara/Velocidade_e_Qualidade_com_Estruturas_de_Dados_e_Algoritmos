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

lista = ["lápis", "caneta", "borracha", "caderno", "livro"]
print(lista)
print(bubbleSort(lista))