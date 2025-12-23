"""Sequência de Fibonacci
Gere os primeiros N termos da sequência de Fibonacci, onde N é fornecido pelo usuário."""

n = int(input("Digite um numero: ").strip())
fibonacci = ["1"]
soma = 0
somaAtual = 1
proximaSoma = 0

for i in range(2 , n + 1):
    fibonacci.append(somaAtual)
    proximaSoma = somaAtual
    somaAtual += soma
    soma = proximaSoma

seqFibo = " x ".join(map(str, fibonacci))
print(f"A seguencia de fibonacci e {seqFibo}")