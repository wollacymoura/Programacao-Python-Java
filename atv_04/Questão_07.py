import random

def simulador_dados():
    dado = random.randint(1, 6)
    print(f"Você rolou o número: {dado}")

def menu_dados():
    while True:
        print("\n--- Simulador de Dados ---")
        simulador_dados()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_dados()