# Dados dois conjuntos:

# python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Calcule e mostre:

# A união de A e B

# A interseção de A e B

# A diferença entre A e B

# A diferença simétrica entre A e B
uniao = A|B
print(uniao)
intersecao = A&B
print(intersecao)
diferenca = A-B
print(diferenca)
diferenca_simetrica= A^B
print(diferenca_simetrica)