from Classe import *

def main():

    tarefas = ToDoList("itens, adicionar tarefas")

    x = 0
    while x!= 0:

        try:
            print("O que você deseja realizar?\n1 - Adicionar Tarefa\n2 - Excluir Tarefa\n3 - Listar Tarefa")

            menu = int(input(">>"))

            match menu:

                case 1:
                    print("--- VOCÊ ESTÁ EM ADICIONAR TAREFAS, DIGITE O QUE DESEJA ADICIONAR A SUA LISTA ---")
                    print (input(">>"))
                    print("")
                    print("FOI ADICIONADO A SUA LISTA")
                    # tarefas.adicionar_tarefa(descrição)

                case 2:
                    print("---VOCÊ ESTÁ EM EXCLUIR TAREFAS, DIGITE O QUE DESEJA EXCLUIR DA SUA LISTA ")
                    print (input(">>"))
                    print("")

                case 3:
                    print("---VOCÊ ESTÁ EM LISTAR TAREFAS, ESTÁ É SUA LISTA! ")
                    print (input(">>"))
                    print("")

                case 4:
                    if x != 0:
                        print ("Saindo do software")

                case _:
                    print  ("Valor inválido")

        except Exception as erro:
            print(f"O erro é: {erro.__class__.__name__}")