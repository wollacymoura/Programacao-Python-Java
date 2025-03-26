numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O primeiro número é o maior, {numero_1}")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O segundo número é o maior, {numero_2}")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(f"O terceiro número é o maior, {numero_3}")

if numero_1 < numero_2 and numero_1 < numero_3:
    print(f"O primeiro número é o menor, {numero_1}")
elif numero_2 < numero_1 and numero_1 < numero_3:
    print(f"O segundo número é o menor, {numero_2}")
elif numero_3 < numero_1 and numero_3 < numero_2:
    print(f"O terceiro número é o menor, {numero_3}")