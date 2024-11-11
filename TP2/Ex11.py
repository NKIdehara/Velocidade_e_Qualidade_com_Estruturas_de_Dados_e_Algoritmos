class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if len(self.fila) > 0:
            cliente = self.fila.pop(0)
            print("Cliente atendido: " + cliente)
        else:
            print("Nenhum cliente na fila.")

    def tamanho_fila(self):
        return len(self.fila)

fila = FilaAtendimento()
fila.adicionar_cliente("Fulano")
fila.adicionar_cliente("Beltrano")
fila.adicionar_cliente("Ciclano")

print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()
fila.atender_cliente()
print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()
print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()