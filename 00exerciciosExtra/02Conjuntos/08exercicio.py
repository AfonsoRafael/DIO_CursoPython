"""Nível 4: Desafio
Exercício 4.1
Escreva uma função que simule a recomendação de amigos em uma rede social:

Você tem um conjunto de amigos: seus_amigos

Cada amigo tem um conjunto de amigos: amigos_de_amigos

Recomende amigos que:

Não são seus amigos atuais

São amigos de pelo menos 2 dos seus amigos

Retorne os recomendados ordenados alfabeticamente"""


def __init__(amigos,amigos_amigos):
    pass

def perfil():
    print("""
-------------REDE SOCIAL-------------
    [1] ADICIONAR USUARIO
    [2] SELECIONAR USUARIO
    [3] EXCLUIR USUARIO
    [4] LISTAR REDE
              """)
    return int(input("Digite a acao que deseja fazer: ").strip)

def usuario(usuario):
    print(f"""
-------------REDE SOCIAL {usuario}-------------
    [1] ADICIONAR AMIGO
    [2] RECOMENDACOES
    [3] EXCLUIR AMIGO
    [4] LISTAR AMIGOS
              """)
    return int(input("Digite a acao que deseja fazer: "))

def adiciona_usuario(rede):
    nome = input("Digite o nome do usuario que deseja adicionar: ")
    if nome in rede:
        print(f"Usuario {nome} ja existe!!!")
    else:
        rede.append(nome)
        nome = set()
        print("Usuario criado com sucesso!!!")


def main():
    rede = {}
    n = perfil()
    
    rede = adiciona_usuario(rede)
    pass