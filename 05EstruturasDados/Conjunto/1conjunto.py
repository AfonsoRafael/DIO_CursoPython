# O conjunto em Python é uma coleção não ordenada de elementos únicos.
# Ele é mutável, o que significa que você pode adicionar ou remover elementos após a criação.
# Conjuntos são úteis para operações matemáticas como união, interseção e diferença.

# Criando conjuntos
conjunto_a = set([1, 2, 3, 4, 5, 1, 2, 3])  # Conjunto criado a partir de uma lista, duplicatas serão removidas
conjunto_b = {4, 5, 6, 7, 8}       # Conjunto criado usando chaves
conjunto_vazio = set()               # Conjunto vazio
letras = set("python")            # Conjunto criado a partir de uma string
numeros = set(range(5))           # Conjunto criado a partir de um range
print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)
print("Conjunto Vazio:", conjunto_vazio)
print("Letras:", letras)
print("Números:", numeros)

# Acessando elementos do conjunto
# Conjuntos não suportam indexação ou fatiamento, pois são não ordenados
# É preciso converter para lista ou tupla para acessar elementos por índice
conjunto_lista = list(conjunto_a)
print("Primeiro elemento do Conjunto A (convertido para lista):", conjunto_lista[0])

# Iterando sobre conjuntos
print("Iterando sobre Conjunto B:")
for elemento in conjunto_b:
    print(elemento)

# Função enumerate para obter índice e valor
print("Iterando com índice usando enumerate em Conjunto A:")
for indice, elemento in enumerate(conjunto_a):
    print(f"Índice {indice}: Elemento {elemento}")