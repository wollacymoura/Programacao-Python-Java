numero = 2
quantidade_numero = 0

while quantidade_numero < 100:
    verificacao = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            verificacao = False
            break
    if verificacao:
        print(f"O {quantidade_numero}° número primo é: {numero}")
        quantidade_numero +=1
    numero += 1