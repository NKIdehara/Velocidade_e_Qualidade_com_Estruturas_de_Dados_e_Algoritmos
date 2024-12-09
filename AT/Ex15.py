class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir_valor(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_novo(self.raiz, valor)

    def _inserir_novo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_novo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_novo(no.direita, valor)

    def minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.valor

arvore = Arvore()
lista = [85,70,95,60,75,90,100]
for i in lista:
    arvore.inserir_valor(i)
print(f"valor mínimo: {arvore.minimo()}")
print(f"valor máximo: {arvore.maximo()}")
