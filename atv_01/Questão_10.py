numero = int(input("Digite um número inteiro maior que 1: "))

verificacao = True
if numero < 2: 
    eh_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:
            verificacao = False
            break

if verificacao:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")