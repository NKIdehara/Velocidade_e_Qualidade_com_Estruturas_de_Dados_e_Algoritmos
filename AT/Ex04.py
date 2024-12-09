import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None
        self.iteracoes = 0

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

    def buscar(self, valor):
        return self._buscar_no(self.raiz, valor), self.iteracoes
    
    def _buscar_no(self, no, valor):
        self.iteracoes += 1
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar_no(no.esquerda, valor)
        else:
            return self._buscar_no(no.direita, valor)

def busca_lista(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return True, i
    return False, len(lista)

arvore = Arvore()
lista = []

for i in range(100000):
    valor = random.randint(1000000000, 9999999999)
    arvore.inserir_valor(valor)
    lista.append(valor)
arvore.inserir_valor(7777777777)
lista.append(7777777777)
print(arvore.buscar(7777777777))
print(busca_lista(lista, 7777777777))