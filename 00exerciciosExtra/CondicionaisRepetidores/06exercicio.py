# Solicite um número ao usuário e exiba a tabuada desse número de 1 a 10.

print("---Tabuada de um número---")
n = int(input("Digite um numero para ver a tabuada: ").strip())
        
print("Tabuada de %d:" % n)
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado }")