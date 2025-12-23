"""Nível Avançado
Calculadora de IMC com Classificação
Calcule o Índice de Massa Corporal (IMC = peso / altura²) e classifique:
Abaixo de 18.5: Abaixo do peso

18.5-24.9: Peso normal

25-29.9: Sobrepeso

30-34.9: Obesidade grau 1

35-39.9: Obesidade grau 2

Acima de 40: Obesidade grau 3

"""
print("---Calculo do imc---")
peso = float(input("Informe o seu peso: "))
altura=float(input("Informe a sua altura: "))
imc = peso/(altura*altura)
if imc > 40:
    print("Obesidade grau 3")
elif 35 < imc<39.9:
    print("Obesidade grua 2")
elif 30 < imc<34.9:
    print("Obesidade grau 1")
elif 25<imc<29.9:
    print("Sobrepeso")
elif 20<imc<24.9:
    print("Peso normal")
else:
    print("Abaixo do peso")