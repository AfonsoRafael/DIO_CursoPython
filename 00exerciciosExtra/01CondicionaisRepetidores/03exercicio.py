# Desenvolva uma calculadora que receba dois números e uma operação (+, -, *, /) e retorne o resultado. Trate a divisão por zero

print("---Calculadora Simples---")
num1 = float(input("Digite o primeiro numero: ").strip())
num2 = float(input("Digite o segundo numero: ").strip())
operacao = input("Digite a operacao (+, -, *, /): ").strip()

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} e: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} e: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} e: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} e: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma das operações (+, -, *, /).")  