# Gerenciador de Contatos

import json

# carregar a lista de contatos do arquivo .json, se não existir, retorna uma lista vazia
def carregar_contatos():
    try:
        with open('contatos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# salva uma lista de contatos no arquivo .json
def salvar_contatos(contatos):
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

# adiciona um novo contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!")

# busca os contatos pelo nome
def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    contatos = carregar_contatos()
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print("Contato não encontrado.")

# mostra todos os contatos já registrados na lista
def listar_contatos():
    contatos = carregar_contatos()
    print("\n=== Lista de Contatos ===")
    if contatos:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato encontrado.")

# controle de ações do usuário
def sistema_contatos():
    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar todos os contatos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            buscar_contato()
        elif escolha == "3":
            listar_contatos()
        elif escolha == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

# chamada da função
sistema_contatos()