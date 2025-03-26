quilometragem = int(input("Qual a quilometragem total percorrida? "))
dias = int(input("Qual a quantidade de dias que ele percorreu: "))

if quilometragem > 100:
    valor_total = (quilometragem - 100) * 12
    valor_total = valor_total + (dias * 90)
    print(f"o valor a ser pago é de: {valor_total} reais.")
else:
    valor_total = dias * 90
    print(f"o valor a ser pago é de: {valor_total} reais.")