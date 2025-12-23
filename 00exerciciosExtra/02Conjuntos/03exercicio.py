"""Nível 2: Intermediário
Exercício 2.1
Em uma escola, os alunos do time de futebol são: {Ana, Bruno, Carla, Daniel}
Os alunos do time de vôlei são: {Carla, Daniel, Elena, Fabio}
Encontre:
a) Alunos que estão nos dois times
b) Alunos que estão apenas no time de futebol
c) Alunos que estão apenas no time de vôlei
d) Todos os alunos que participam de pelo menos um time"""

futebol = {"Ana", "Bruno", "Carla", "Daniel"}
volei = {"Carla", "Daniel", "Elena", "Fabio"}

intercecao = futebol.intersection(volei)
print(f"Alunos que jogam futebol e volei: {intercecao}")

sofut = futebol.difference(volei)
print(f"So jogam futebol: {sofut}")

sovolei= volei.difference(futebol)
print(f"So jogam volei: {sovolei}")

uniao = futebol.union(volei)
print(f"Praticam pelo menos um esporte: {uniao}")