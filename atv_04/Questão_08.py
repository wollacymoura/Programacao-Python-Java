def verificar_palindromo():
    palavra = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

def menu_palindromo():
    while True:
        print("\n--- Verificador de Palíndromos ---")
        verificar_palindromo()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_palindromo()