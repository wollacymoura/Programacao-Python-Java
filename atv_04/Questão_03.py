def contar_caracteres():
    frase = input("Digite uma frase: ")
    caracteres = len(frase.replace(" ", ""))
    print(f"A frase tem {caracteres} caracteres (sem considerar espaços).")

def menu_contagem():
    while True:
        print("\n--- Contador de Caracteres ---")
        contar_caracteres()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_contagem()