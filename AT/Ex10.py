class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []
        self.atual = None

    def carregar(self, pagina):
        if self.atual is not None:
            self.pilha_voltar.append(self.atual)
        self.pilha_avancar.clear()
        self.atual = pagina
        print(f"página atual: {self.atual}")

    def voltar(self):
        if len(self.pilha_voltar) == 0:
            print("\nVOLTAR: Operação inválida!")
            print(f"página atual: {self.atual}")
            return
        self.pilha_avancar.append(self.atual)
        self.atual = self.pilha_voltar.pop()
        print(f"\nVOLTAR\npágina atual: {self.atual}")

    def avancar(self):
        if len(self.pilha_avancar) == 0:
            print("\nAVANÇAR: Operação inválida!")
            print(f"página atual: {self.atual}")
            return
        self.pilha_voltar.append(self.atual)
        self.atual = self.pilha_avancar.pop()
        print(f"\nAVANÇAR\npágina atual: {self.atual}")

navegador = Navegador()
navegador.carregar("infnet.edu.br")
navegador.carregar("python.org")
navegador.carregar("fedoraproject.org")
navegador.avancar()
navegador.voltar()
navegador.avancar()
navegador.voltar()
navegador.voltar()
navegador.voltar()
navegador.carregar("microsoft.com")
navegador.avancar()
navegador.voltar()
