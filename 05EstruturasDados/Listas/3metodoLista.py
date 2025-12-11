frutas = ["maça", "banana", "cereja"] # Lista de frutas
idades = [25, 30, 35, 40, 30 , 30 , 35, 30] # Lista de idades
mista = ["texto", 42, 3.14, True]      # Lista mista com diferentes tipos de dados
vazia = [] # Lista vazia
letras = list("python") # Lista criada a partir de uma string
numeros = list(range(5)) # Lista criada a partir de um range

# Usando métodos de lista
print("Lista original de frutas:", frutas)

# Adicionando um item ao final da lista
frutas.append("laranja")
print("Após append:", frutas)

# Limpando a lista
frutas.clear()
print("Após clear:", frutas)

# Copiando a lista de idades
idades_copiadas = idades.copy()
print("Cópia da lista de idades:", idades_copiadas)
print("Lista original de idades:", idades)
print(id(idades_copiadas), id(idades))  # Verifica se são objetos diferentes

# Contando ocorrências de um valor
ocorrencias_30 = idades.count(30)
print("Ocorrências de 30 na lista de idades:", ocorrencias_30)

# Adicionando múltiplos itens com extend
idades.extend([45, 50, 30])
print("Após extend:", idades)

# Encontrando o índice de um valor
indice_35 = idades.index(35)
print("Índice da primeira ocorrência de 35:", indice_35)

# Removendo um item com pop, sem argumento remove o último, conceito de pilha (LIFO)
idade_removida = idades.pop()
print("Idade removida com pop:", idade_removida)
print("Após pop:", idades)

# Removendo um item específico
idades.remove(30)  # Remove a primeira ocorrência de 30
print("Após remove(30):", idades)

# Invertendo a lista
idades.reverse()
print("Após reverse:", idades)

# Ordenando a lista
idades.sort()
print("Após sort:", idades)
# Ordenando a lista em ordem decrescente
idades.sort(reverse=True)
print("Após sort(reverse=True):", idades)
# Ordenando por tamanho de string
frutas = ["maça", "kiwi", "banana", "cereja", "abacaxi"]
frutas.sort(key=lambda fruta: len(fruta))
print("Frutas ordenadas por tamanho:", frutas)
# Ordenando por tamanho de string em ordem decrescente
frutas.sort(key=lambda fruta: len(fruta), reverse=True)
print("Frutas ordenadas por tamanho (decrescente):", frutas)

# Verificando o tamanho da lista
tamanho_idades = len(idades)
print("Tamanho da lista de idades:", tamanho_idades)

