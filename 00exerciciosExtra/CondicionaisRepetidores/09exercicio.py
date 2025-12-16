#Calcule o fatorial de um número inteiro fornecido pelo usuário usando um loop.

# inline suggest enabled
"""
Para desativar as sugestões da IA:
Encontre a opção: "Editor - Inline Suggest: Enabled"

Desmarque a caixa de seleção (clique nela para remover o ✔)

Ela deve ficar assim: [ ] (vazia) em vez de [✔]

Passo adicional recomendado:
Também desmarque:

"Editor - Inline Suggest: Syntax Highlighting Enabled" (opcional, mas recomendado)
"""
print("----Fatorial de um numero---")

n = int(input("Digite um numero para ser mostrado o seu fatorial: ").strip())

fatorial = 1

for i in range(1, n+1):
    fatorial = i * fatorial
    i += 1
print(f"O valor da fatorial de {n} e: {fatorial}")