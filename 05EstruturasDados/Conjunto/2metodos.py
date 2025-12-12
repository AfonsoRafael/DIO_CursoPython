conjunto_a = set([1, 2, 3, 4, 5])
conjunto_b = {4, 5, 6, 7, 8}
conjunto_vazio = set()

# Métodos úteis para conjuntos

# union(): Retorna a união de dois conjuntos
uniao = conjunto_a.union(conjunto_b)
print("União de A e B:", uniao)

# intersection(): Retorna a interseção de dois conjuntos
intersecao = conjunto_a.intersection(conjunto_b)
print("Interseção de A e B:", intersecao)

# difference(): Retorna a diferença entre dois conjuntos
diferenca = conjunto_a.difference(conjunto_b)
print("Diferença de A e B (A - B):", diferenca)
diferenca_ba = conjunto_b.difference(conjunto_a)
print("Diferença de B e A (B - A):", diferenca_ba)

# symmetric_difference(): Retorna a diferença simétrica entre dois conjuntos
diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print("Diferença simétrica entre A e B:", diferenca_simetrica)

# issubset(): Verifica se um conjunto é subconjunto de outro
subconjunto = {1, 2}
eh_subconjunto = subconjunto.issubset(conjunto_a)
print("O conjunto {1, 2} é subconjunto de A?", eh_subconjunto)
# issuperset(): Verifica se um conjunto é superconjunto de outro
eh_superconjunto = conjunto_a.issuperset(subconjunto)
print("O conjunto A é superconjunto de {1, 2}?", eh_superconjunto)

# isdisjoint(): Verifica se dois conjuntos são disjuntos (sem elementos em comum)
conjunto_c = {9, 10}
sao_disjuntos = conjunto_a.isdisjoint(conjunto_c)
print("Os conjuntos A e C são disjuntos?", sao_disjuntos)

# add(): Adiciona um elemento ao conjunto
conjunto_a.add(6)
print("Conjunto A após adicionar 6:", conjunto_a)

# remove(): Remove um elemento do conjunto (gera erro se o elemento não existir)
conjunto_a.remove(3)
print("Conjunto A após remover 3:", conjunto_a)

# discard(): Remove um elemento do conjunto (não gera erro se o elemento não existir)
conjunto_a.discard(10)  # 10 não está em A, mas não gera erro
print("Conjunto A após descartar 10 (sem erro):", conjunto_a)

# pop(): Remove e retorna um elemento arbitrário do conjunto
elemento_removido = conjunto_a.pop()
print("Elemento removido de A usando pop():", elemento_removido)
print("Conjunto A após pop():", conjunto_a)

# clear(): Remove todos os elementos do conjunto
conjunto_b.clear()
print("Conjunto B após clear():", conjunto_b)

# copy(): Retorna uma cópia rasa do conjunto
conjunto_copia = conjunto_a.copy()
print("Cópia do Conjunto A:", conjunto_copia)

# len(): Retorna o número de elementos no conjunto
tamanho_conjunto = len(conjunto_a)
print("Tamanho do Conjunto A:", tamanho_conjunto)

# in: Verifica se um elemento está no conjunto
existe_4 = 4 in conjunto_a
print("O número 4 está no Conjunto A?", existe_4)
existe_10 = 10 in conjunto_a
print("O número 10 está no Conjunto A?", existe_10)
