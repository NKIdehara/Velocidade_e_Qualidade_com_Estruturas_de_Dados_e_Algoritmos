class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela_chave = []
        self.tabela_valor = []

    def inserir(self, chave, valor):
        if len(self.tabela_chave) >= self.tamanho:
            print("Tabela Hash esgotada.")
            return
        
        for i in range(len(self.tabela_chave)): # verifica se chave já existe
            if self.tabela_chave[i] == chave:
                self.tabela_valor[i] = valor
                return

        self.tabela_chave.append(chave)
        self.tabela_valor.append(valor)

    def buscar(self, chave):
        for i in range(len(self.tabela_chave)):
            if self.tabela_chave[i] == chave:
                return self.tabela_valor[i]
        return "chave não encontrada."

    def remover(self, chave):
        for i in range(len(self.tabela_chave)):
            if self.tabela_chave[i] == chave:
                print(self.tabela_chave[i] + " removida")
                self.tabela_chave.pop(i)
                self.tabela_valor.pop(i)
                return
        print("chave não encontrada.")

tabela = TabelaHash(3)
tabela.inserir("chave 1", "valor 1")
tabela.inserir("chave 2", "valor 2")
tabela.inserir("chave 3", "valor 3")
print("chave 1: " + tabela.buscar("chave 1"))
print("chave 2: " + tabela.buscar("chave 2"))
print("chave 3: " + tabela.buscar("chave 3"))
print("chave 4: " + tabela.buscar("chave 4"))
tabela.inserir("chave 4", "valor 4")
tabela.remover("chave 2")
tabela.inserir("chave 4", "valor 4")
print("chave 1: " + tabela.buscar("chave 1"))
print("chave 2: " + tabela.buscar("chave 2"))
print("chave 3: " + tabela.buscar("chave 3"))
print("chave 4: " + tabela.buscar("chave 4"))
