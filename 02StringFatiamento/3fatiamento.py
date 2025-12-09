# Fatiamento de strings em Python
# Sintaxe: string[início:fim:passo]
frase = "Curso em Video Python"
print(frase[0:5])      # Do índice 0 ao 4 (5 não incluso)
print(frase[10:15])    # Do índice 10 ao 14 (15 não incluso)
print(frase[:5])       # Do início ao índice 4
print(frase[10:])      # Do índice 10 até o final
print(frase[::2])     # Do início ao fim, pulando de 2 em 2
print(frase[1::2])    # Do índice 1 ao fim, pulando de 2 em 2
print(frase[::-1])    # Inverte a string
print(frase[5::-1])   # Do índice 5 ao início, invertido
print(frase[-1])      # Último caractere