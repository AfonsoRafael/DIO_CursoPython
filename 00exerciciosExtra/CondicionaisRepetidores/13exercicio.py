"""
 Adivinhe o Número
Implemente um jogo onde o computador gera um número aleatório entre 1 e 100, e o usuário tenta adivinhar. O programa deve dar dicas "muito alto" ou "muito baixo" até o acerto.
"""
import random
print("---Descubra o numero de 1 a 100---")

sorteado = random.randint(1,100)
escolhido =1
while sorteado != escolhido:
    escolhido = int(input("Digite o numero que voce acredita ser o certo: "))
    if escolhido > sorteado:
        print("O numero sorteado e menor que o escolhido")
    elif escolhido < sorteado:
        print("O numero sorteado e maior que o escolhido")
    
print("Parabens por acertar o numero!!!")