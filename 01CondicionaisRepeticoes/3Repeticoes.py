# Estruturas de repetições em Python são usadas para executar um bloco de código várias vezes, enquanto uma condição for verdadeira ou por um número específico de vezes.
# As principais estruturas de repetição em Python são o loop "for" e o loop "while".
# O loop "for" é usado para iterar sobre uma sequência (como listas, tuplas, dicionários, conjuntos ou strings).
# O loop "while" é usado para executar um bloco de código enquanto uma condição for verdadeira.
# Exemplo de loop "for" para iterar sobre uma lista:
print("Exemplo de loop 'for' para iterar sobre uma lista:")
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
print("----------------------------------------------------\n\n")
# Exemplo de loop "while" para repetir enquanto uma condição for verdadeira:
print("Exemplo de loop 'while' para repetir enquanto uma condição for verdadeira:")
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
print("----------------------------------------------------\n\n")
# Exemplo de loop "for" com a função range() para repetir um número específico de vezes:
print("Exemplo de loop 'for' com a função range() para repetir um número específico de vezes:")
for i in range(1, 6):
    print(f"Número: {i}")
print("----------------------------------------------------\n\n")
# Exemplo de loop "while" com uma condição de parada:
print("Exemplo de loop 'while' com uma condição de parada:")
soma = 0
while True:
    numero = int(input("Digite um número para adicionar à soma (ou 0 para parar): "))
    if numero == 0:
        break
    soma += numero
print(f"A soma total é: {soma}")
print("----------------------------------------------------\n\n")
# Exemplo de loop "for" para iterar sobre um dicionário:
print("Exemplo de loop 'for' para iterar sobre um dicionário:")
idades = {"Alice": 25, "Bob": 30, "Charlie": 35}
for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos")
print("----------------------------------------------------\n\n")
# Exemplo de loop "while" com a instrução continue:
print("Exemplo de loop 'while' com a instrução continue:")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")
print("----------------------------------------------------\n\n")
# Exemplo de loop "for" aninhado:
print("Exemplo de loop 'for' aninhado:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
print("----------------------------------------------------\n\n")
# Função range() com parâmetros adicionais:
print("Função range() com parâmetros adicionais:") 
for numero in range(10, 0, -2):
    print(f"Número: {numero}")
print("----------------------------------------------------\n\n")
# Exemplo de loop "while" com else:
print("Exemplo de loop 'while' com else:")
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("O loop 'while' terminou normalmente.")
print("----------------------------------------------------\n\n")
# Break e continue em loops:
print("Break e continue em loops:")
for numero in range(1, 11):
    if numero == 5:
        print("Encontrado o número 5, saindo do loop.")
        break
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")
print("----------------------------------------------------\n\n")