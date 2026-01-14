"""
Exercício 1: Crie uma lista com os números de 1 a 10 e faça:

Adicione o número 11 ao final

Insira o número 0 no início

Remova o número 5 da lista

Inverta a ordem dos elementos

Crie uma nova lista apenas com números pares da lista original
"""
numero = list(range(1,11))

numero.append(11)
print(numero)
numero.insert(0,0)
print(numero)
print(numero.pop(5))
print(numero)
numero.sort(reverse = True)
print(numero)

pares = [x for x in numero if x % 2 == 0]
print(pares)