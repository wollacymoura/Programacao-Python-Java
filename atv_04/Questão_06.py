def contar_vogais():
    texto = input("Digite uma palavra ou frase: ")
    vogais = "aeiouAEIOU"
    contagem = sum(1 for char in texto if char in vogais)
    print(f"O texto contém {contagem} vogais.")

def menu_vogais():
    while True:
        print("\n--- Contador de Vogais ---")
        contar_vogais()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_vogais()