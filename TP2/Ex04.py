def ordena_pilha(origem, destino):
    aux = []

    # encerra recursao
    if len(origem) == 0:
        return
    
    if len(destino) > 0:
        if origem[-1] > destino[-1]: # ultimo elemento da origem é maior do que o ultimo do destino
            destino.append(origem.pop())
        else:
            while len(destino) > 0: # tira os elementos do destino (e coloca no aux) até o ultimo da origem ser o maior do que sobrou do destino
                if origem[-1] > destino[-1]:
                    break
                aux.append(destino.pop())
            destino.append(origem.pop())
            while len(aux) > 0: # devolve os elementos do aux para o destino
                destino.append(aux.pop())
    else:
        destino.append(origem.pop())
    ordena_pilha(origem, destino)


lista = [7.4, 2.0, 6.6, 2.5, 2.9, 8.2, 1.6, 6.7, 2.8, 6.1, 0.9, 4.2, 4.8, 0.0, 0.8, 8.2, 6.9, 8.4, 5.1, 1.3, 1.2, 1.5, 2.0, 3.6, 0.1, 0.3, 4.9, 4.8, 6.9, 7.5, 4.4, 0.4, 8.8, 2.6, 5.1, 3.5, 5.1, 0.0, 5.8, 4.4, 0.9, 6.8, 10.0, 9.6, 5.5, 1.9, 9.6, 8.3, 8.5, 2.6, 7.7, 5.0, 9.9, 1.4, 8.4, 8.1, 2.9, 5.1, 5.7, 2.1, 9.4, 3.1, 1.6, 2.4, 3.7, 0.8, 0.2, 3.4, 7.5, 1.0, 6.4, 7.4, 4.5, 7.2, 9.3, 6.5, 9.8, 2.5, 9.9, 4.5, 2.0, 1.2, 2.2, 7.9, 4.6, 6.3, 8.2, 6.0, 9.7, 0.4, 8.3, 6.5, 4.0, 0.5, 6.4, 7.0, 9.8, 6.0, 6.3, 9.8]
destino = []
ordena_pilha(lista, destino)
print(destino)

