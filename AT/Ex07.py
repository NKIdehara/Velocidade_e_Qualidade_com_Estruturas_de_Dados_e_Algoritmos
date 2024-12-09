def procura_duplicatas(lista):
    duplicata = False
    duplicatas = {}
    for i in lista:
        if i in duplicatas:
            duplicatas[i] += 1
            duplicata = True
        else:
            duplicatas[i] = 1
    return duplicata

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(procura_duplicatas(lista))