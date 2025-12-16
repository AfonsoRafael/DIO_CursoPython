"""
 Contador de Vogais
Faça um programa que conte quantas vogais (a, e, i, o, u) existem em uma string fornecida pelo usuário.
"""
frase= input("Digite uma frase que mostraremos a quantidade de vogais: ")
vogais = "aeiou"
q = 0
for letra in frase:
    if letra in vogais:
        q+=1
print(f"Qauntidade de vogais e {q}")