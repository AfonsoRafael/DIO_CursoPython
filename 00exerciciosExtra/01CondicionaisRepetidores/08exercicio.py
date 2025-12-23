"""Escreva um programa que converta uma nota (0-100) em conceitos:

90-100: A

80-89: B

70-79: C

60-69: D

0-59: F"""

print("---Conversão de nota para conceito---")
nota = int(input("Digite a nota (0-100): ").strip())

if 90 <= nota <= 100:
    conceito = 'A'
elif 80 <= nota <= 89:
    conceito = 'B'
elif 70 <= nota <= 79:
    conceito = 'C'
elif 60 <= nota <= 69:
    conceito = 'D'
else:
    conceito = 'F'

print(f"A nota {nota} corresponde ao conceito: {conceito}")