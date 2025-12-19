# As funções são blocos de código que podem ser reutilizados em diferentes partes do programa. Elas permitem organizar o código em partes menores e mais legíveis, facilitando a manutenção e a reutilização.
# Os parâmetros são valores que podem ser passados para as funções para que elas possam operar com esses valores.
# As funções podem retornar valores usando a palavra-chave return.
def saudacao(nome):
    return f"Olá, {nome}!"
def soma(a, b):
    return a + b
def exibir_mensagem():
    print("Esta é uma mensagem sem parâmetros e sem retorno.")
def exibir_saudacao(nome="Afonso"):
    print(f"Olá, {nome}!")
# Chamando as funções
print(saudacao("Maria"))  # Saída: Olá, Maria!
print(soma(5, 3))        # Saída: 8 
exibir_mensagem()        # Saída: Esta é uma mensagem sem parâmetros e sem retorno.
exibir_saudacao()        # Saída: Olá, Afonso!
exibir_saudacao("João")  # Saída: Olá, João!

# None é um valor especial em Python que representa a ausência de valor. Quando uma função não retorna explicitamente um valor, ela retorna None por padrão.
def funcao_sem_retorno():
    print("Esta função não retorna nada.")
resultado = funcao_sem_retorno()
print(resultado)  # Saída: None

# Argumentos nomeados permitem passar valores para os parâmetros de uma função especificando o nome do parâmetro, o que torna o código mais legível e flexível.
def apresentar(nome, idade):
    return f"Meu nome é {nome} e tenho {idade} anos."
print(apresentar(idade=25, nome="Ana"))  # Saída: Meu nome é Ana e tenho 25 anos.

# Args e Kwargs são usados para passar um número variável de argumentos para uma função.
# Args (argumentos posicionais) são passados como uma tupla, enquanto Kwargs (argumentos nomeados) são passados como um dicionário.
def funcao_varios_args(*args, **kwargs): # importante usar o * e ** para indicar args e kwargs
    print("Args:", args)
    print("Kwargs:", kwargs)

funcao_varios_args(1, 2, 3, nome="Carlos", idade=30)