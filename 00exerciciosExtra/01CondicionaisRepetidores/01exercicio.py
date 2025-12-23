# Verificação de números pares ou ímpares
print("---Verificação de números pares ou ímpares---")
n = int(input("Digite um numero: ").strip())

if n % 2 == 0:
    print(f"O numero {n} e par.")
else:
    print(f"O numero {n} e impar.")