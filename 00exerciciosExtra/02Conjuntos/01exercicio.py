"""Nível 1: Básico
Exercício 1.1
Crie um conjunto contendo os dias da semana: segunda, terça, quarta, quinta, sexta.
Crie outro conjunto com os dias de fim de semana: sábado, domingo.
Verifique se os dois conjuntos são disjuntos e mostre o resultado"""

semana = {"segunda", "terca","quarta","quinta","sexta" }
fim_semana = {"sabado","domingo"}

disjuncao = semana.isdisjoint(fim_semana)

print(f"Os conjuntos sao conjuntos? {disjuncao}")
