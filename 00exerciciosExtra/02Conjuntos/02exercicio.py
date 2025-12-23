"""Exercício 1.2
Dado o conjunto numeros = {1, 3, 5, 7, 9}, faça:
a) Adicione o número 11
b) Remova o número 3
c) Verifique se o número 7 está no conjunto
d) Mostre o tamanho do conjunto após as operações"""

numeros = {1, 3, 5, 7, 9}
print(numeros)
numeros.add(11)
print(numeros)
numeros.remove(3)
print(numeros)
verifica = 7 in numeros
print(verifica)
print(len(numeros))

