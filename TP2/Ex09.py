def ordena_fila(origem, destino):
    aux = []

    # encerra recursao
    if len(origem) == 0:
        return
    
    if len(destino) > 0:
        if origem[0] > destino[-1]: # primeiro elemento da origem é maior do que o ultimo do destino
            destino.append(origem.pop(0))
        else:
            while len(destino) > 0: # tira os elementos do destino (e coloca no aux) até o primeiro da origem ser o maior do que sobrou do destino
                if origem[0] > destino[-1]:
                    break
                aux.append(destino.pop())
            destino.append(origem.pop(0))
            while len(aux) > 0: # devolve os elementos do aux para o destino
                destino.append(aux.pop())
    else:
        destino.append(origem.pop(0))
    ordena_fila(origem, destino)

lista = [4, 0, 7, 9, 6, 3, 2, 7, 8, 1, 5, 8, 4, 3, 3, 7, 2, 1, 7, 3]
print(lista)
destino = []
ordena_fila(lista, destino)
print(destino)