import time
import random

def mochila_recursiva(capacidade, pesos, valores, n):
    if n == 0 or capacidade == 0:
        return 0
    if (pesos[n-1] > capacidade):
        return mochila_recursiva(capacidade, pesos, valores, n-1)
    else:
        return max(valores[n-1] + mochila_recursiva(capacidade-pesos[n-1], pesos, valores, n-1), mochila_recursiva(capacidade, pesos, valores, n-1))

def mochila_recursiva_memoria(capacidade, pesos, valores, n, memoria):
    # implementação de memorização / consulta memória
    if (capacidade, n) in memoria:
        return memoria[(capacidade, n)]
    
    if n == 0 or capacidade == 0:
        return 0
    if (pesos[n-1] > capacidade):
        return mochila_recursiva_memoria(capacidade, pesos, valores, n-1, memoria)
    else:
        resultado = max(valores[n-1] + mochila_recursiva_memoria(capacidade-pesos[n-1], pesos, valores, n-1, memoria), mochila_recursiva_memoria(capacidade, pesos, valores, n-1, memoria))
    
    # implementação de memorização / armazena memória
    memoria[(capacidade, n)] = resultado
    return resultado

pesos = []
valores = []
for i in range(0, 71, 1):
    pesos = pesos + [random.randint(1, 99) for _ in range(1)]
    valores = valores + [random.randint(1, 99) for _ in range(1)]
    capacidade = 150
    t_1 = time.time()
    resultado1 = mochila_recursiva(capacidade, pesos, valores, len(pesos))
    t_2 = time.time()
    resultado2 = mochila_recursiva_memoria(capacidade, pesos, valores, len(pesos), {})
    t_3 = time.time()
    print(f"Num. elementos: {len(pesos)}\tTempo (recursivo): {(t_2 - t_1):.2f}\tTempo (memória): {(t_3 - t_2):.2f}\t{resultado1} {resultado2}")
