import time
import random

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def calcula_tempo_bubble_sort(lista):
    t_ini = time.time()
    resultado = bubble_sort(lista[:])
    t_fim = time.time()
    print(f"Num. elementos: {len(lista)}\tTempo de execução: {(t_fim - t_ini):.2f}")
    return resultado

lista = [17, 10, 17, 11, 20, 18, 14, 3, 15, 13]
print(f"Lista de teste: {lista}")
print(f"Resultado: {calcula_tempo_bubble_sort(lista)}\n")

for i in range(1000, 10001, 1000):
    lista = [random.randint(1, 99999) for _ in range(i)]
    calcula_tempo_bubble_sort(lista)