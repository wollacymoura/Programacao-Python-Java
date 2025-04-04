def gerar_tabuada():
    numero = int(input("Digite um número para gerar a tabuada: "))
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def menu_tabuada():
    while True:
        print("\n--- Gerador de Tabuada ---")
        gerar_tabuada()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_tabuada()