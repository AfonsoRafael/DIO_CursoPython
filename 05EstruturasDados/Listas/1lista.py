# Listas são estruturas de dados que armazenam uma coleção ordenada de itens.
# Elas são mutáveis, o que significa que você pode alterar seus elementos após a criação.

frutas = ["maca", "banana", "cereja"] # Lista de frutas
idades = [25, 30, 35, 40]              # Lista de idades
mista = ["texto", 42, 3.14, True]      # Lista mista com diferentes tipos de dados
vazia = []                        # Lista vazia
letras = list("python") # Lista criada a partir de uma string
numeros = list(range(5)) # Lista criada a partir de um range

print("Frutas:", frutas)
print("Idades:", idades)
print("Lista mista:", mista)
print("Lista vazia:", vazia)
print("Letras:", letras)
print("Números:", numeros)

# Acessando elementos da lista
# A indexação começa em 0
# Inicial/final/passo podem ser usados para fatiar listas
print("Primeira fruta:", frutas[0])        # Acessa o primeiro elemento
print("Ultima idade:", idades[-1])         # Acessa o último elemento
print("Segmento de frutas:", frutas[1:3])  # Acessa um segmento da lista
print("Todas as idades:", idades[:])      # Acessa todos os elementos
print("Idades a partir do segundo elemento:", idades[1:]) # Acessa a lista a partir do segundo elemento
print("Letras em passos de 2:", letras[::2]) # Acessa elementos com passo de 2
print("Números invertidos:", numeros[::-1]) # Acessa a lista de trás para frente

# Matriz 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Acessando elementos em uma matriz
print("Elemento na linha 1, coluna 2 da matriz:", matriz[1][2]) # Acessa o elemento 6
print("Segunda linha da matriz:", matriz[1]) # Acessa a segunda linha da matriz
print("Primeira coluna da matriz:", [linha[0] for linha in matriz]) # Acessa a primeira coluna da matriz
print("Matriz invertida:", matriz[::-1]) # Acessa a matriz de trás para frente
