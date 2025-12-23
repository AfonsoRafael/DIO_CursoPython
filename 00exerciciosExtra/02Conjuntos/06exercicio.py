"""Implemente um sistema de controle de estoque onde:

Quando um produto é vendido, ele é removido do conjunto de disponíveis

Quando um produto chega, ele é adicionado ao conjunto

Não pode haver produtos duplicados no estoque

Crie funções para:

Adicionar produto ao estoque

Remover produto do estoque (apenas se existir)

Verificar se um produto está disponível

Mostrar todos os produtos em ordem alfabética"""

def menu():
    print("""
    ---------------SISTEMA DE VENDAS---------
    [1] ADICIONAR PRODUTO
    [2] REMOVER PRODUTO
    [3] VERIFICAR SE O PRODUTO ESTA DISPONIVEL
    [4] MOSTRAR PRODUTOS
    [0] SAIR
          """)
    return input("Digite a opcao que deseja: ").strip()

def adicionar(produto):
    adiciona = input("Digite o produto que deseja adicionar: ")
    quant = int(input("Informe a quantidade: "))
    if adiciona in produto:
        produto[adiciona] += quant
        print("---------Quantidade atualizada---------")
    else:
        produto[adiciona] = quant
        print("---------Produto cadastrado----------")
def remover(produto):
    remove = input("Informe o nome do produto que deseja remover: ").strip()
    if remove in produto:
        quant = int(input("Informe a quantidade que deseja remover: "))
        if produto[remove] < quant:
            print("Valor maior que o estoque!!!")
        else:
            produto[remove] -= quant
            if produto[remove] == 0:
                item_removido = produto.pop(remove)
                print(f"Produto removido com sucesso: {item_removido}")
            else:
                print(f"Produto atualizado: {remove} {produto[remove]}")
    else:
        print("Nao temos esse produto cadastrado!!!")

def listar(produto):
    produtos = sorted(produto.items())
    print("Produtos e valores")
    for chave, valor in produtos:
        print(f"{chave}: {valor}")

def verificar(produto):
    verifica = input("Digite o produto que deseja consultar:")
    if verifica in produto:
        print(f"Temos o produto {verifica} com {produto[verifica]} de estoque")
    else:
        print("Nao temos esse produto")

def main():
    produto = {}

    
    while True:
        n = menu()
        if n == "1":
            adicionar(produto)
        elif n == "2":
           remover(produto)
        elif n == "3":
            verificar(produto)
        elif n == "4":
            listar(produto)
        elif n == "0":
            break
        else:
            print("Valor invalido!!!")

main()