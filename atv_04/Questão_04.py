def calcular_media():
    notas = []
    for i in range(3):
        notas.append(float(input(f"Digite a nota {i + 1}: ")))
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7 else "Reprovado"
    print(f"A média do aluno é {media:.2f}. Status: {status}.")

def menu_media():
    while True:
        print("\n--- Calculadora de Média ---")
        calcular_media()
        sair = input("Deseja sair? (s para sim / qualquer tecla para não): ")
        if sair.lower() == "s":
            break

menu_media()