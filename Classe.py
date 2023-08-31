class ToDoList():
    def __init__(self, itens):
        self.itens = itens
        self.adicionar = []

class Inf(ToDoList):

    def adicionar_tarefa(self, descrição):
        descrição = descrição
        self.adicionar.append(descrição)

    def excluir_tarefa(self, indice):
        indice = indice
        self.adicionar_tarefa


    def listar_tarefas(self):
        pass