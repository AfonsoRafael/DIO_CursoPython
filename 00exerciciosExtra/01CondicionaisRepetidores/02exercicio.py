# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

print("---Maior e Menor Número---")
num1 = float(input("Digite o primeiro numero:").strip())
num2 = float(input("Digite o segundo numero: ").strip())
num3 = float(input("Digite o terceiro numero: ").strip())

if (num1 >= num2) and (num1 >= num3):
    maior = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        menor = num2
        medio = num3
elif (num2 >= num1) and (num2 >= num3):
    maior = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        menor = num1
        medio = num3
else:
    maior = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        menor = num1
        medio = num2

print(f"O maior numero e: {maior}")
print(f"O numero do meio e: {medio}")
print(f"O menor numero e: {menor}")