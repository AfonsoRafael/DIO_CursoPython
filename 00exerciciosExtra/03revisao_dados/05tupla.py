""" Escreva uma função que recebe duas tuplas de coordenadas (x1, y1) e (x2, y2)
 e retorna a distância euclidiana entre elas."""
import os

def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    
    # Cálculo da distância euclidiana
    euclidiana = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    print(f"O valor da euclidiana dos pontos é {euclidiana:.2f}")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        # Usando map(int, ...) para converter cada item da lista em inteiro
        ponto1 = tuple(map(int, input("Digite os pontos da posicao 1 (x,y): ").strip().split(",")))
        # list comprehesion mesmo resultado porem mais eficiente
        ponto2 = tuple(int(valor) for valor in input("Digite os pontos da posicao 2 (x,y): ").strip().split(","))

        calcular_distancia(ponto1, ponto2)
    except ValueError:
        print("Erro: Digite apenas números separados por vírgula (ex: 10,20).")

    opcao = input("Deseja verificar mais pontos? [s][n] ").strip().lower()
    if opcao == 'n':
        break