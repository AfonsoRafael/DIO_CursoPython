# Parametros especiais em funcoes
def funcao_exemplo(a, b=2, *args, c=3, **kwargs):
    print(f"a: {a}")          # Parâmetro obrigatório
    print(f"b: {b}")          # Parâmetro com valor padrão
    print(f"args: {args}")    # Argumentos posicionais adicionais
    print(f"c: {c}")          # Parâmetro com valor padrão nomeado
    print(f"kwargs: {kwargs}") # Argumentos nomeados adicionais
# Chamando a função com diferentes tipos de argumentos
funcao_exemplo(1, 4, 5, 6, c=7, nome="Ana", idade=28)
# Saída:
# a: 1
# b: 4
# args: (5, 6)
# c: 7
# kwargs: {'nome': 'Ana', 'idade': 28}

# parametros especials em funcoes podem ser por posicao ou nomeados
def funcao_posicao_nomeado(x, y=10,/,*, z=20):
    print(f"x: {x}")  # Parâmetro obrigatório por posição
    print(f"y: {y}")  # Parâmetro com valor padrão por posição
    print(f"z: {z}")  # Parâmetro nomeado obrigatório
# Chamando a função
funcao_posicao_nomeado(5, z=30)

# Objetos de primeira classe
# Em Python, funções são objetos de primeira classe, o que significa que podem ser atribuídas a variáveis, passadas como argumentos para outras funções e retornadas por outras funções.
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def operacao(func, x, y):
    return func(x, y)
resultado_soma = operacao(soma, 5, 3)
resultado_subtracao = operacao(subtracao, 5, 3)
print(f"Soma: {resultado_soma}")              # Saída: Soma: 8
print(f"Subtração: {resultado_subtracao}")    # Saída: Subtração: 2

# Escopo local e global
# Variáveis definidas dentro de uma função têm escopo local e não podem ser acessadas fora dela. Variáveis definidas fora de qualquer função têm escopo global e podem ser acessadas dentro das funções, mas para modificá-las é necessário usar a palavra-chave global.
x = 10  # Variável global
def funcao_escopo():
    global x
    x = 20  # Modificando a variável global
    y = 5   # Variável local
    print(f"Variável local y: {y}")  # Saída: Variável local y: 5
funcao_escopo()
print(f"Variável global x: {x}")  # Saída: Variável global
