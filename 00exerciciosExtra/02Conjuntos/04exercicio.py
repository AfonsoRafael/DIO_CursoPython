"""Exercício 2.2
Um professor aplicou uma prova e quer saber:

Alunos que acertaram a questão 1: {A1, A3, A5, A7}

Alunos que acertaram a questão 2: {A2, A3, A6, A7}

Alunos que acertaram a questão 3: {A1, A4, A5, A7}

Encontre:
a) Alunos que acertaram todas as questões
b) Alunos que acertaram pelo menos uma questão
c) Alunos que acertaram apenas uma questão
d) Alunos que não acertaram nenhuma questão (supondo que a turma tem alunos A1 a A10)"""

alunos = {"A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"}
Q1 = {"A1","A3","A5","A7"}
Q2 = {"A2","A3","A6","A7"}
Q3 = {"A1","A4","A5","A7"}
todas = set()

for aluno in alunos:
    if aluno in Q1 and aluno in Q2 and aluno in Q3:
        todas.add(aluno)
print(f"Os alunos que acertaram todas as questoes foram: {", ".join(todas)}")

apenas1 = Q1.symmetric_difference(Q2.union(Q3))

print(f"Alunos que acertaram apenas uma questao: {", ".join(apenas1)}")

peloMenos1 = Q1.union(Q2.union(Q3))

print(f"Alunos que tiveram pelo menos 1 acerto: {", ".join(peloMenos1)}")

nenhum = alunos.difference(peloMenos1)

print(f"Alunos que nao acertaram nada: {", ".join(nenhum)}")