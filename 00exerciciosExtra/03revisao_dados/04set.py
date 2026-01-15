"""Crie um programa que verifica se uma lista de palavras contém duplicatas
 usando conjuntos. O programa deve retornar True se houver palavras repetidas
 e False caso contrário."""

import os
lista = []
while True:
    palavra = input("Digite uma palavra para adicionar na lista: ")
    lista.append(palavra)
    opcao = input("Deseja adicionar mais uma palavra? [s][n]  ").strip().lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == "n":
        break


conj = set(lista)
repedito = True
for palavra in lista:
    if palavra in conj:
        conj.remove(palavra)
    else:
        repedito = False

print(repedito)
print(f"{lista}")