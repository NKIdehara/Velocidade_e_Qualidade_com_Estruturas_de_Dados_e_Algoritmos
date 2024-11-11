def tarefa_no_topo(pilha_de_tarefas):
    if len(pilha_de_tarefas) > 0:
        return pilha_de_tarefas[-1]
    return "Não há tarefas na pilha."

lista = ["Lavar o carro", "Limpar a casa", "Estudar Ciência da Computação"]
# lista = []
print("A tarefa mais recente é: " + tarefa_no_topo(lista))