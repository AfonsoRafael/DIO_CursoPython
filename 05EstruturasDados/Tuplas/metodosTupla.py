frutas = ("maca", "banana", "cereja",) # Tupla de frutas
idades = tuple([1,5,6,8,10,22,41])              # Tupla de idades
mista = ("texto", 42, 3.14, True,)      # Tupla mista com diferentes tipos de dados
vazia = ()                        # Tupla vazia
letras = tuple("python") # Tupla criada a partir de uma string
numeros = tuple(range(5)) # Tupla criada a partir de um range

# Métodos úteis para tuplas

# count(): Retorna o número de ocorrências de um elemento na tupla
num_cerejas = frutas.count("cereja")
print("Número de cerejas na tupla de frutas:", num_cerejas)

# index(): Retorna o índice da primeira ocorrência de um elemento na tupla
indice_banana = frutas.index("banana")
print("Índice da banana na tupla de frutas:", indice_banana)

# len(): Retorna o número de elementos na tupla
tamanho_tupla = len(idades)
print("Tamanho da tupla de idades:", tamanho_tupla)