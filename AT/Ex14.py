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

    def buscar(self, valor):
        return self._buscar_no(self.raiz, valor)
    
    def _buscar_no(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor < no.valor:
            return self._buscar_no(no.esquerda, valor)
        else:
            return self._buscar_no(no.direita, valor)

arvore = Arvore()
lista = [100,50,150,30,70,130,170]
for i in lista:
    arvore.inserir_valor(i)
print(arvore.buscar(70))
