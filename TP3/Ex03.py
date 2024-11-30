def mostrar_torre(origem, auxiliar, destino):
    i = len(origem)
    j = len(auxiliar)
    k = len(destino)
    for t in range(i+j+k, -1, -1):
        print(f"{origem[t] if i > t else "|"}\t{auxiliar[t] if j > t else "|"}\t{destino[t] if k > t else "|"}")
    print("")

def mover_peca(origem, destino):
    destino.append(origem.pop())

def torre_hanoi(n, origem, auxiliar, destino):
    if n == 1:
        mover_peca(origem, destino)
        return
    torre_hanoi(n-1, origem, destino, auxiliar) # (1)
    mover_peca(origem, destino)                 # (2)
    torre_hanoi(n-1, auxiliar, origem, destino) # (3)

origem = ["C", "B", "A"]
auxiliar = []
destino = []
mostrar_torre(origem, auxiliar, destino)
torre_hanoi(len(origem), origem, auxiliar, destino)
mostrar_torre(origem, auxiliar, destino)
