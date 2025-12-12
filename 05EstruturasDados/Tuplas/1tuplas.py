# Diferença entre Listas e Tuplas em Python
# Listas são mutáveis, ou seja, seus elementos podem ser alterados, adicionados ou removidos.
# Tuplas são imutáveis, ou seja, uma vez criadas, seus elementos não podem ser alterados, adicionados ou removidos.
# Boa pratica em tuplas é colocar virgula no final

# Criando uma tupla
frutas = ("maca", "banana", "cereja",) # Tupla de frutas
idades = tuple([1,5,6,8,10,22,41])              # Tupla de idades
mista = ("texto", 42, 3.14, True,)      # Tupla mista com diferentes tipos de dados
vazia = ()                        # Tupla vazia
letras = tuple("python") # Tupla criada a partir de uma string
numeros = tuple(range(5)) # Tupla criada a partir de um range

print("Frutas:", frutas)

# Acessando elementos da tupla
# A indexação começa em 0
print("Primeira fruta:", frutas[0])        # Acessa o primeiro elemento
print("Ultima idade:", idades[-1])         # Acessa o último elemento
print("Segmento de frutas:", frutas[1:3])  # Acessa um segmento da tupla
print("Todas as idades:", idades[:])      # Acessa todos os elementos
print("Idades a partir do segundo elemento:", idades[1:]) # Acessa a tupla a partir do segundo elemento
print("Letras em passos de 2:", letras[::2]) # Acessa elementos com passo de 2
print("Numeros invertidos:", numeros[::-1]) # Acessa a tupla de trás para frente

# Desempacotamento de tuplas
fruta1, fruta2, fruta3 = frutas
print("Fruta 1:", fruta1)
print("Fruta 2:", fruta2)
print("Fruta 3:", fruta3)

# Matriz 
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)
# Acessando elementos em uma matriz
print("Elemento na linha 1, coluna 2 da matriz:", matriz[1][2]) # Acessa o elemento 6
print("Segunda linha da matriz:", matriz[1]) # Acessa a segunda linha da matriz
print("Primeira coluna da matriz:", [linha[0] for linha in matriz]) # Acessa a primeira coluna da matriz
print("Matriz invertida:", matriz[::-1]) # Acessa a matriz de trás para frente
