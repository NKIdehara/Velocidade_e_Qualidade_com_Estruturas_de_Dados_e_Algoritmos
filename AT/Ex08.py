def selection_sort(lista):
    for i in range(len(lista)):
        indice = i
        for j in range(i + 1, len(lista)):
            if lista[j][1] < lista[indice][1]:
                indice = j
        lista[i], lista[indice] = lista[indice], lista[i]
    return lista

lista = []
lista.append(["Ana", 54])
lista.append(["Bruno", 61])
lista.append(["Carlos", 74])
lista.append(["Daniela", 30])
lista.append(["Eduardo", 28])
lista.append(["Fernanda", 77])
lista.append(["Gabriel", 63])
lista.append(["Helena", 57])
lista.append(["Igor", 43])
lista.append(["Juliana", 39])
print(selection_sort(lista))