def converter_km_milhas():
    km = float(input("Digite a quantidade de quilômetros: "))
    print(f"{km} km é igual a {km * 0.621371:.2f} milhas.")

def converter_metros_cm():
    metros = float(input("Digite a quantidade de metros: "))
    print(f"{metros} metros é igual a {metros * 100} centímetros.")

def converter_litros_ml():
    litros = float(input("Digite a quantidade de litros: "))
    print(f"{litros} litros é igual a {litros * 1000} mililitros.")

def menu_conversor():
    while True:
        print("\n--- Conversor de Unidades ---")
        print("1. Converter quilômetros para milhas")
        print("2. Converter metros para centímetros")
        print("3. Converter litros para mililitros")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            converter_km_milhas()
        elif escolha == "2":
            converter_metros_cm()
        elif escolha == "3":
            converter_litros_ml()
        elif escolha == "4":
            print("Saindo do conversor...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_conversor()