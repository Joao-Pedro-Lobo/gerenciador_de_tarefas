import csv
import os
from datetime import datetime
def verificar_arquivo():
    if not os.path.exists("tarefas.csv"):
        with open("tarefas.csv", "w", newline="") as arquivo:
            pass  # Cria o arquivo vazio

def menu():
    verificar_arquivo()
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Remover tarefa")
        print("5. Marcar tarefa como concluída")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            editar_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            concluir_tarefa()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("tarefas.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([descricao, data, "pendente"])

    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    try:
        with open("tarefas.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            print("\n=== Lista de Tarefas ===")
            for i, linha in enumerate(leitor):
                if linha:  # ignora linhas vazias
                    descricao, data, status = linha
                    print(f"{i+1}. {descricao} | {status} | Criado em: {data}")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def editar_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para editar: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    with open("tarefas.csv", "r") as arquivo:
        tarefas = list(csv.reader(arquivo))

    if 0 <= indice < len(tarefas):
        nova_desc = input("Nova descrição: ")
        tarefas[indice][0] = nova_desc

        with open("tarefas.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(tarefas)

        print("Tarefa editada com sucesso.")
    else:
        print("Índice inválido.")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    with open("tarefas.csv", "r") as arquivo:
        tarefas = list(csv.reader(arquivo))

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)

        with open("tarefas.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(tarefas)

        print("Tarefa removida com sucesso.")
    else:
        print("Índice inválido.")

def concluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    with open("tarefas.csv", "r") as arquivo:
        tarefas = list(csv.reader(arquivo))

    if 0 <= indice < len(tarefas):
        tarefas[indice][2] = "concluída"

        with open("tarefas.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(tarefas)

        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

if __name__ == "__main__":
    menu()
