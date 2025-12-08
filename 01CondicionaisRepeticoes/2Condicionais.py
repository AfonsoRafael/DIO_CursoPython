# A estrurura condicional em Python é feita utilizando as palavras-chave if, elif e else.
# A estrutura condicional permite executar diferentes blocos de código com base em condições específicas.
# A palavra-chave if é usada para testar uma condição inicial.
# A palavra-chave elif (else if) é usada para testar condições adicionais se a condição if for falsa.
# A palavra-chave else é usada para definir um bloco de código que será executado se todas as condições anteriores forem falsas.
# Exemplo de estrutura condicional com if, elif e else:
print("Exemplo de estrutura condicional com if, elif e else:")
numero = int(input("Digite um numero: "))
if numero > 20:
    print("O numero e maior que 20")
elif numero > 10:
    print("O numero e maior que 10, mas 20 ou menor")
else:
    print("O numero e 10 ou menor")

# if alinhado, if dentro de if
# Exemplo de múltiplas estruturas condicionais alinhadas:
print("----------------------------------------------------\n\n")
print("Exemplo de múltiplas estruturas condicionais alinhadas:")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Voce e maior de idade.")
    if idade >= 65:
        print("Voce e um idoso.")
    else:
        print("Voce e um adulto.")
else:
    print("Voce e menor de idade.")

# if ternário
# A estrutura condicional ternária em Python permite atribuir valores com base em uma condição em uma única linha. É composta pela expressão condicional seguida por um valor se verdadeiro e outro se falso. Utilizado para simplificar atribuições condicionais.
# Exemplo de if ternário para atribuição condicional:
print("----------------------------------------------------\n\n")
print("Exemplo de if ternário para atribuição condicional:")
numero = int(input("Digite um numero: "))
resultado = "Par" if numero % 2 == 0 else "Impar"
print(f"O numero {numero} é {resultado}.")

