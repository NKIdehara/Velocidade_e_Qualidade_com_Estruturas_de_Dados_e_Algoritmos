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

    def remover_valor(self, valor):
        self.raiz = self._remover_valor(self.raiz, valor)

    def _remover_valor(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerda = self._remover_valor(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_valor(no.direita, valor)
        else: # remover valor
            if no.esquerda is None and no.direita is None: # não possui filhos
                return None
            elif no.esquerda is None: # somente um filho
                return no.direita
            elif no.direita is None:  # somente um filho
                return no.esquerda
            else: # possui dois filhos
                novo_pai = self._minimo_no(no.direita)
                no.valor = novo_pai.valor
                no.direita = self._remover_valor(no.direita, novo_pai.valor)
        return no

    def _minimo_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def exibir_arvore(self):
        def _exibir_valor_no(no):
            if no is not None:
                _exibir_valor_no(no.esquerda)
                print(no.valor, end=' ')
                _exibir_valor_no(no.direita)
        _exibir_valor_no(self.raiz)
        print()

arvore = Arvore()
lista = [45,25,65,20,30,60,70]
for i in lista:
    arvore.inserir_valor(i)
arvore.exibir_arvore()
arvore.remover_valor(20)
arvore.exibir_arvore()
arvore.remover_valor(25)
arvore.exibir_arvore()
arvore.remover_valor(45)
arvore.exibir_arvore()
