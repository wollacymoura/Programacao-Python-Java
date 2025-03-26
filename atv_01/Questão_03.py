valor_mercadoria = float(input("Qual o valor total das mercadorias compradas? "))

if valor_mercadoria < 500:
    print(f"Após a avaliação, suas mercadorias foram avaliadas em {valor_mercadoria} reais")
else:
    imposto = valor_mercadoria * (50/100)
    valor_mercadoria = valor_mercadoria + imposto
    print(f"Após a avaliação, suas mercadorias foram avaliadas em {valor_mercadoria} reais")