'''Interpolação de variáveis em strings
- Utilizando f-strings (Python 3.6+)
- Utilizando o método format()
- Utilizando o operador %
'''
# Utilizando f-strings (Python 3.6+)
nome = "João"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos.")  # f-string
# Ou com expressões
print(f"Daqui a 5 anos, {nome} terá {idade + 5} anos.")  # f-string com expressões
# Com formatação de dicionários
pessoa = {"nome": "Maria", "idade": 30}
print(f"Meu nome é {pessoa['nome']} e eu tenho {pessoa['idade']} anos.")  # f-string com dicionário

# Com .format() para formatação de números
preco = 49.99
print(f"O preço do produto é R$ {preco:10.2f}.")  # f-string com formatação de número


# Utilizando o método format()
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))  # método format()

# Ou com índices
# Vantegem de usar índices é poder reutilizar os mesmos valores em diferentes posições  da string
print("Meu nome é {0} e eu tenho {1} anos.".format(nome, idade))  # método format() com índices

# Utilizando o operador %
# tipo de dados: %s para strings, %d para inteiros, %f para floats
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))  # operador %

# Metodo format mais antigo
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade))  # método format() com nomes dos parâmetros
print("-" * 50)
nome2 = "Afonso"
idade2 = 23
profissao = "Programador"
linguagem = "Python"

dados = {"nome2": "Afonso", "idade2": 23, "profissao": "Programador", "linguagem": "Python"}

print("Nome: %s Idade: %d Profissao: %s Linguagem: %s" % (nome2, idade2, profissao, linguagem))  # operador % com múltiplos valores

print("Nome: {} Idade: {} Profissao: {} Linguagem: {}".format(nome2, idade2, profissao, linguagem))  # método format() com múltiplos valores

print("Nome: {0} Idade: {1} Profissao: {2} Linguagem: {3}".format(nome2, idade2, profissao, linguagem))  # método format() com índices

print("Nome: {nome2} Idade: {idade2} Profissao: {profissao} Linguagem: {linguagem}".format(nome2=nome2, idade2=idade2, profissao=profissao, linguagem=linguagem))  # método format() com nomes dos parâmetros

print("Nome: {nome2} Idade: {idade2} Profissao: {profissao} Linguagem: {linguagem}".format(**dados))  # método format() com dicionário desempacotado

print(f"Nome: {nome2} Idade: {idade2} Profissao: {profissao} Linguagem: {linguagem}")  # f-string com múltiplos valores

