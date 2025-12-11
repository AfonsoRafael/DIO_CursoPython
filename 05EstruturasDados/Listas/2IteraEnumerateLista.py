frutas = ["maça", "banana", "cereja"] # Lista de frutas
idades = [25, 30, 35, 40]              # Lista de idades
mista = ["texto", 42, 3.14, True]      # Lista mista com diferentes tipos de dados
vazia = []                        # Lista vazia
letras = list("python") # Lista criada a partir de uma string
numeros = list(range(5)) # Lista criada a partir de um range

# Iterando sobre listas
print("Iterando sobre frutas:")
for fruta in frutas:
    print(fruta) # Imprime cada fruta na lista

# Função enumerate para obter índice e valor
print("\nIterando com indice usando enumerate:")
for indice, idade in enumerate(idades):
    print(f"Indice {indice}: Idade {idade}") # Imprime o índice e a idade correspondente

# Usando list comprehension para criar uma nova lista
quadrados = [x**2 for x in numeros]
print("\nLista de quadrados dos numeros:", quadrados) # Imprime a lista de quadrados
# Criando filtração com list comprehension
pares = [x for x in numeros if x % 2 == 0]
print("Numeros pares:", pares) # Imprime a lista de números pares