# Decoradores em Python

# Um decorador é uma função que recebe outra função como argumento,
# adiciona algum tipo de funcionalidade a ela e retorna uma nova função.

# Inner function é uma função definida dentro de outra função.
print("Exemplo de decoradores e inner functions em Python")
print("-----------------------------------------------")
print("Exemplo 1: Decoradores simples")
def mensagem(nome):
    print("Antes da saudacaoo")
    return f"Oi {nome}!"
def mensagemLonga(nome):
    print("Executando mensagem longa...")
    return f"Ola, tudo bem {nome}?"

def executor(func):
    print("Iniciando execucao da funcaoo...")
    return func
def executar(funcao, nome): # funcao que recebe outra funcao e um nome como argumentos
    print("Preparando para executar a funcao...")
    resultado = funcao(nome)
    print("Execucao concluida.")
    return resultado

print(executor(mensagem)("Maria")) # Chama executor, que retorna a funcao mensagem, que é chamada com "Maria", 
print(executar(mensagemLonga, "Joao"))



print("-----------------------------------------------")
print("Exemplo 2: Inner Functions")
def principal():
    print("Oi da funcao principal!")
    def secundaria(): # funcao escopada, inner function nao acessivel fora de principal
        print("Oi do inner function! funcao secundaria")
    def secundaria2():
        print("Oi do inner function! funcao secundaria2")

    secundaria()
    secundaria2()

principal()

# Tambem é possivel retornar uma função de dentro de outra função.
print("-----------------------------------------------")
print("Exemplo 3: Retornando funcoes")
def calcular(operacao):
    def soma(a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplicacao(a, b):
        return a * b
    def divisao(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao
        case _:
            return None
        
print(calcular("+")(5, 3)) # Chama calcular, que retorna a funcao soma, que é chamada com 5 e 3
print(calcular("-")(10, 4)) # Chama calcular, que retorna a funcao subtracao, que é chamada com 10 e 4
print(calcular("*")(6, 7)) # Chama calcular, que retorna a funcao multiplicacao, que é chamada com 6 e 7
print(calcular("/")(20, 5)) # Chama calcular, que retorna a funcao divisao, que é chamada com 20 e 5

op = calcular("+")
print(op(15, 25)) # Chama a funcao soma retornada por calcular com 15 e 25
op = calcular("*")
print(op(3, 4)) # Chama a funcao multiplicacao retornada por calcular com 3 e 4
op = calcular("-")
print(op(100, 30)) # Chama a funcao subtracao retornada por calcular com 100 e 30
op = calcular("/")
print(op(81, 9)) # Chama a funcao divisao retornada por calcular com 81 e 9

print("-----------------------------------------------")
print("Exemplo 4: Decoradores")
def decorador(func):
    def envelope():
        print("Antes da execucao da funcao decorada.")
        func()
        print("Depois da execucao da funcao decorada.")
    return envelope

def minha_funcao():
    print("Oi da funcao decorada!")

@decorador
def minha_func():# Usando o decorador com a sintaxe @, acucar sintatico
    print("Oi da funcao decorada! Usando @decorador")


minha_funcao = decorador(minha_funcao) # Aplica o decorador a minha_funcao
minha_funcao() # Chama a funcao decorada
minha_func() # Chama a funcao decorada usando o @decorador