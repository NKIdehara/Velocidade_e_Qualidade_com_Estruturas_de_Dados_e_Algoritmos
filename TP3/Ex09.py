class No_Arvore:
    def __init__(self, valor, esquerda = None, direita = None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def valor_arvore(raiz):
    if raiz is None:
        return "-"
    return [valor_arvore(raiz.esquerda), raiz.valor, valor_arvore(raiz.direita)]

raiz = No_Arvore("A")
raiz.esquerda = No_Arvore("B")
raiz.direita = No_Arvore("C")
raiz.esquerda.esquerda = No_Arvore("D")
raiz.esquerda.direita = No_Arvore("E")
print(valor_arvore(raiz))