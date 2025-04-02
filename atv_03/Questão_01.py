# Gerenciador de Tarefas Melhorado

import json

# carregar o arquivo .json, caso não exista, retorna com uma lista vazia
def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# salva a lista de tarefas dentro do arquivo .json
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# adicionar uma nova tarefa com descrição e prazo
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    prazo = input("Digite o prazo da tarefa (formato AAAA-MM-DD): ")
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# lista todas as tarefas ordenadas pelo prazo
def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas_ordenadas = sorted(tarefas, key=lambda t: t["prazo"])
    for tarefa in tarefas_ordenadas:
        estado = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{tarefa['descricao']} - {tarefa['prazo']} - {estado}")

# permite marcar alguma tarefa como concluida
def marcar_concluida():
    descricao = input("Digite a descrição da tarefa a ser marcada como concluída: ")
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["descricao"] == descricao:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
            return
    print("Tarefa não encontrada.")

# controle de ações do usuário
def sistema_gerenciador_tarefas():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            marcar_concluida()
        elif escolha == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# chamada da função
sistema_gerenciador_tarefas()