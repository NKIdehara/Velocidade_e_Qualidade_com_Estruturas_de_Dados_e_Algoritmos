class Contatos:
    def __init__(self):
        # lista[0] -> lista de nomes
        # lista[1] -> lista de telefones
        self.lista = [[],[]]

    def incluir(self, nome, telefone):
        self.lista[0].append(nome)
        self.lista[1].append(telefone)

    def buscar(self, nome):
        for i, contato in enumerate(self.lista[0]):
            if nome in contato:
                return self.lista[1][i]
        return "Não encontrado!"

contatos = Contatos()
contatos.incluir("Ana Silva", "23-4567-8901")
contatos.incluir("Bruno Costa", "11-2345-6789")
contatos.incluir("Carlos Oliveira", "32-1234-5678")
contatos.incluir("Daniela Pereira", "24-0123-4567")
contatos.incluir("Eduardo Santos", "18-9012-3456")
contatos.incluir("Fernanda Lima", "67-8901-2345")
contatos.incluir("Gabriel Souza", "56-7890-1234")
contatos.incluir("Helena Almeida", "45-6789-0123")
contatos.incluir("Igor Fernandes", "34-5678-9012")
contatos.incluir("Juliana Rocha", "12-3456-7890")

print(contatos.buscar("Silva"))