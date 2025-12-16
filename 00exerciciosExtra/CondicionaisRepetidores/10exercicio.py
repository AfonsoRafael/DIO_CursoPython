# Verifique se um número fornecido pelo usuário é primo ou não.

print("---Verificacao de numero primo---")
n = int(input("Digite um numero e verifique se e primo: ").strip())
primo = True
for i in range(2,n):
    if n%i == 0:
        primo = False 

if primo == True :
    print(f"O numero {n} e primo!")
else:
    print(f"O numero {n} nao e primo")

"""

16. Média de Notas
Peça ao usuário para inserir notas até que ele digite -1. Em seguida, calcule e mostre a média das notas digitadas.

Nível Avançado
17. Calculadora de IMC com Classificação
Calcule o Índice de Massa Corporal (IMC = peso / altura²) e classifique:

Abaixo de 18.5: Abaixo do peso

18.5-24.9: Peso normal

25-29.9: Sobrepeso

30-34.9: Obesidade grau 1

35-39.9: Obesidade grau 2

Acima de 40: Obesidade grau 3

18. Número Perfeito
Verifique se um número é perfeito (um número perfeito é aquele que é igual à soma dos seus divisores próprios positivos, excluindo ele mesmo).

19. Pirâmide de Números
Peça um número N e imprima uma pirâmide de números como no exemplo para N=5:

text
1
22
333
4444
55555
20. Menu Interativo
Crie um programa com o seguinte menu:

Calcular área do quadrado

Calcular área do círculo

Calcular área do triângulo

Sair

O programa deve continuar exibindo o menu até que o usuário escolha a opção 4.

21. Contagem Regressiva Inteligente
Faça uma contagem regressiva de um número fornecido pelo usuário até 0. Se o número for maior que 20, conte de 2 em 2; se for maior que 10, conte de 1 em 1; caso contrário, conte mostrando apenas os números pares.

22. Sistema de Login
Implemente um sistema de login com as seguintes funcionalidades:

Cadastrar novo usuário (nome, senha)

Fazer login

Sair

Armazene os dados em um dicionário. Permita até 3 tentativas de login.

Desafios
23. Jogo da Forca
Implemente o jogo da forca. O programa deve escolher uma palavra secreta e o usuário tem 6 tentativas para adivinhar as letras.

24. Simulador de Caixa Eletrônico
Crie um simulador de caixa eletrônico que permita:

Consultar saldo

Sacar valor (não permitir saque maior que saldo)

Depositar valor

Sair

Comece com um saldo inicial de R$ 1000,00.

25. Analisador de Números
Peça ao usuário para digitar vários números (até digitar 0). Em seguida, mostre:

Quantos números foram digitados

A média dos números

O maior e o menor número

Quantos são pares e quantos são ímpares"""