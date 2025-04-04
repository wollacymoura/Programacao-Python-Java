def soma():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O resultado de {n1} + {n2} é igual a: {n1 + n2}")

def subtracao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O resultado de {n1} - {n2} é igual a: {n1 - n2}")

def multiplicacao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O resultado de {n1} x {n2} é igual a: {n1 * n2}")

def divisao():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O resultado de {n1} ÷ {n2} é igual a: {n1 / n2}")

def operacao(escolha):
    if escolha == "1":
        soma()
    elif escolha == "2":
        subtracao()
    elif escolha == "3":
        multiplicacao()
    elif escolha == "4":
        divisao()
    elif escolha == "5":
        print("Encerrando a calculadora...")
    else:
        print("Escolha inválida, tente novamente.")

def menu_calculadora():
    while True:
        print("-----Calculadora-----")
        print("escolha uma operação:")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. divisão")
        print("5. sair")
        escolha = input()
        operacao(escolha)
        if escolha == "5":
            break

menu_calculadora()