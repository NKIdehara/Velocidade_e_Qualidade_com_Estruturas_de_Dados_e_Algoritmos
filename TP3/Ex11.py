def fatorial(n):
    if n == 0:
        return 1
    else:
        try:
            valor = n * fatorial(n-1)
            return valor
        except RecursionError as e:
            print(f"Erro na recursão: {e}")
            print(f"Erro calculando n={n}")

def fatorial_iterativo(n):
    valor = 1
    for i in range(1, n + 1):
        valor *= i
    return valor

n = 1500
try:
    print(f"Fatorial de {n}: {fatorial(n)}")
except:
    print("")
print(f"Fatorial iterativo de {n}: {fatorial_iterativo(n)}")
