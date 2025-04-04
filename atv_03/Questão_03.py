# Sistema de Reservas de Eventos

import json

# carregar o mapa dos assentos do arquivo .json
def carregar_assentos():
    try:
        with open('assentos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {f"Assento {i}": False for i in range(1, 51)}

# salva o mapa de assentos dentro do arquivo .json
def salvar_assentos(assentos):
    with open('assentos.json', 'w') as arquivo:
        json.dump(assentos, arquivo, indent=4)

# mostra o estado atual dos assentos
def visualizar_assentos():
    assentos = carregar_assentos()
    for assento, reservado in assentos.items():
        estado = "Reservado" if reservado else "Disponível"
        print(f"{assento}: {estado}")

# rezerva de assentos
def reservar_assento():
    assento = input("Digite o número do assento para reservar (Ex: Assento 1): ")
    assentos = carregar_assentos()
    if assento not in assentos:
        print("Assento inválido.")
    elif assentos[assento]:
        print("Assento já reservado.")
    else:
        assentos[assento] = True
        salvar_assentos(assentos)
        print("Assento reservado com sucesso!")

# cancelar reserva de assento
def cancelar_reserva():
    assento = input("Digite o número do assento para cancelar (Ex: Assento 1): ")
    assentos = carregar_assentos()
    if assento not in assentos:
        print("Assento inválido.")
    elif not assentos[assento]:
        print("Assento já está disponível.")
    else:
        assentos[assento] = False
        salvar_assentos(assentos)
        print("Reserva cancelada com sucesso!")

# controla as ações do usuário
def sistema_reservas():
    while True:
        print("\n=== Sistema de Reservas ===")
        print("1. Visualizar assentos")
        print("2. Reservar assento")
        print("3. Cancelar reserva")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            visualizar_assentos()
        elif escolha == "2":
            reservar_assento()
        elif escolha == "3":
            cancelar_reserva()
        elif escolha == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# chamada da função
sistema_reservas()