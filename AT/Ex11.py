class Atendimento:
    def __init__(self):
        self.fila = []

    def entra(self, cliente):
        self.fila.append(cliente)
        print(f"Novo cliente: {cliente}")
        print(f"Qtde na fila: {len(self.fila)}")

    def atende(self):
        print(f"ATENDIMENTO: {self.fila.pop(0)}")
        print(f"Qtde na fila: {len(self.fila)}")

atendimento = Atendimento()
atendimento.entra("Ana Silva")
atendimento.entra("Bruno Costa")
atendimento.entra("Carlos Oliveira")
atendimento.entra("Daniela Pereira")
atendimento.entra("Eduardo Santos")
atendimento.entra("Fernanda Lima")
atendimento.entra("Gabriel Souza")
atendimento.atende()
atendimento.atende()
atendimento.atende()
atendimento.entra("Helena Almeida")
atendimento.entra("Igor Fernandes")
atendimento.entra("Juliana Rocha")
atendimento.atende()
atendimento.atende()