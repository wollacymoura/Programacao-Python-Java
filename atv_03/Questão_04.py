# Sistema Bancário com Login

import json

# carrega os dados dos usuário do arquivo .json
def carregar_usuarios():
    try:
        with open('usuarios.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# salva o dicionario de usuário dentro do arquivo .json
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

# registra um novo usuário
def registrar_usuario():
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios = carregar_usuarios()
    if username in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[username] = {"senha": senha, "saldo": 0, "transacoes": []}
        salvar_usuarios(usuarios)
        print("Usuário registrado com sucesso!")

# logar em um usuário já cadastrado
def login_usuario():
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios = carregar_usuarios()
    if username in usuarios and usuarios[username]["senha"] == senha:
        print(f"Bem-vindo, {username}!")
        return username
    else:
        print("Usuário ou senha incorretos.")
        return None

# depositar na conta do usuário
def depositar(username):
    valor = float(input("Digite o valor do depósito: "))
    usuarios = carregar_usuarios()
    usuarios[username]["saldo"] += valor
    usuarios[username]["transacoes"].append(f"Depósito de R${valor:.2f}")
    salvar_usuarios(usuarios)
    print("Depósito realizado com sucesso!")

# sacar na conta do usuário
def sacar(username):
    valor = float(input("Digite o valor do saque: "))
    usuarios = carregar_usuarios()
    if usuarios[username]["saldo"] >= valor:
        usuarios[username]["saldo"] -= valor
        usuarios[username]["transacoes"].append(f"Saque de R${valor:.2f}")
        salvar_usuarios(usuarios)
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")

# mostrar o saldo da conta do usuário
def mostrar_saldo(username):
    usuarios = carregar_usuarios()
    saldo = usuarios[username]["saldo"]
    print(f"Saldo atual: R${saldo:.2f}")

# mostra o histórico das transações feitas pelo usuário
def historico_transacoes(username):
    usuarios = carregar_usuarios()
    print("\n=== Histórico de Transações ===")
    for transacao in usuarios[username]["transacoes"]:
        print(transacao)
    if not usuarios[username]["transacoes"]:
        print("Nenhuma transação realizada.")

# controle de ações do usuário
def sistema_bancario():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Registrar usuário")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            registrar_usuario()
        elif escolha == "2":
            username = login_usuario()
            if username:
                while True:
                    print("\n1. Depositar")
                    print("2. Sacar")
                    print("3. Mostrar saldo")
                    print("4. Histórico de transações")
                    print("5. Sair")
                    acao = input("Escolha uma ação: ")
                    if acao == "1":
                        depositar(username)
                    elif acao == "2":
                        sacar(username)
                    elif acao == "3":
                        mostrar_saldo(username)
                    elif acao == "4":
                        historico_transacoes(username)
                    elif acao == "5":
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
        elif escolha == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

# chamada da função
sistema_bancario()