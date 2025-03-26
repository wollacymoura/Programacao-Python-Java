numero_impar = int(input("Escolha um número impar da sua preferência "))

if numero_impar % 2 == 0:
    impar_anterior = numero_impar - 1
    impar_proximo = numero_impar + 1
else:
    impar_anterior = numero_impar - 2
    impar_proximo = numero_impar + 2

numero = (impar_anterior * impar_anterior) - impar_proximo
print(numero)