# Peça ao usuário um número N e calcule a soma de todos os números de 1 até N.

print("---Soma de 1 até N---")
n = int(input("Digite um numero que sera mostrado a progressao aritimetrica ate o numero escolhido: ").strip())
soma = 0

for i in range(1, n+1):
    soma += i
print(f"A progressao aritmetrica de 1 até {n} é: {soma}")