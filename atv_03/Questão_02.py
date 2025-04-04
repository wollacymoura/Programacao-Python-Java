# Controle de Estoque Inteligente

import json

# carregar o arquivo .json, caso não exista, retorna com uma lista vazia
def carregar_estoque():
    try:
        with open('estoque.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# salva a lista de produtos dentro do arquivo .json
def salvar_estoque(produtos):
    with open('estoque.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)

# adiciona na lista um produto com nome, quantidade e preço
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    produtos = carregar_estoque()
    produtos.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(produtos)
    print("Produto adicionado com sucesso!")

# mostra todos os produtos que estão no arquivo .json e da um print no valor total do preço dos produtos dessa lista
def listar_produtos():
    produtos = carregar_estoque()
    valor_total = 0
    for produto in produtos:
        valor_total += produto["quantidade"] * produto["preco"]
        print(f"{produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']:.2f}")
    print(f"Valor total do estoque: R${valor_total:.2f}")

# controle de ações do usuário
def sistema_controle_estoque():
    while True:
        print("\n=== Controle de Estoque ===")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# chamada da função
sistema_controle_estoque()