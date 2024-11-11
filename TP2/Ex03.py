def forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def usando_dicionario(lista):
    frequencia = {}
    duplicados = []

    for item in lista:
        if item in frequencia:
            frequencia[item] += 1
        else:
            frequencia[item] = 1

    for item in frequencia.items():
        if item[1] > 1:
            duplicados.append(item[0])

    return duplicados

lista = [4, 0, 7, 3, 7, 3, 2, 7, 8, 1, 8, 8, 4, 3, 3, 7, 2, 1, 7, 3]
print(forca_bruta(lista))
print(usando_dicionario(lista))
