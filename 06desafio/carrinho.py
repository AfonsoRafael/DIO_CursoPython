# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input("Digite o numero de itens: ").strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("Digite o produto e o valor: ").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho e atualiza o total
    carrinho.append((item, preco))
    total += preco

print("\n--- Carrinho de Compras ---")
for produto, valor in carrinho:
    print(f"{produto}: R$ {valor:.2f}")
print(f"Total: R$ {total:.2f}")
# TODO: Exiba os itens e o total da compra