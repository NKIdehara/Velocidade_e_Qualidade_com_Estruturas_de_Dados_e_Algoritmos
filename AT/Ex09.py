class RedeSocial:
    def __init__(self):
        self.hashtable= {}

    def incluir(self, nome, telefone):
        self.hashtable[nome] = telefone

    def procurar(self, nome):
        return self.hashtable.get(nome)

rede_social = RedeSocial()
rede_social.incluir("Ana Silva", "23-4567-8901")
rede_social.incluir("Bruno Costa", "11-2345-6789")
rede_social.incluir("Carlos Oliveira", "32-1234-5678")
rede_social.incluir("Daniela Pereira", "24-0123-4567")
rede_social.incluir("Eduardo Santos", "18-9012-3456")
rede_social.incluir("Fernanda Lima", "67-8901-2345")
rede_social.incluir("Gabriel Souza", "56-7890-1234")
rede_social.incluir("Helena Almeida", "45-6789-0123")
rede_social.incluir("Igor Fernandes", "34-5678-9012")
rede_social.incluir("Juliana Rocha", "12-3456-7890")
print(rede_social.procurar("Ana Silva"))