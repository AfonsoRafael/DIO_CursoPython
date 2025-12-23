"""Nível 3: Avançado
Exercício 3.1
Escreva uma função que recebe uma lista de números (que pode ter duplicados) e:

Converta para conjunto para remover duplicatas

Retorne uma tupla com:

O conjunto sem duplicatas

Quantos elementos foram removidos

Os elementos únicos em ordem crescente"""

lista = [1,2,3,4,5,6,7,8,9,1,1,1,2,5,2]

listaSemD = set(lista)

tupla = tuple(sorted(listaSemD))

removido = len(lista)- len(listaSemD)
print(f"Lista normal: {lista}")
print(f"Sem duplicados: {list(listaSemD)}")
print(f"Quantidade de itens removidos: {removido}")
print(f"Forma crescente: {", ".join(map(str,tupla))}")