"""Crie uma tupla com informações de 5 livros, onde cada livro
 é representado por uma tupla (titulo, autor, ano). Em seguida:

Acesse o terceiro livro da tupla

Conte quantos livros são de um autor específico (escolhido por você)

Crie uma lista apenas com os títulos dos livros

Verifique se existe um livro com determinado título na tupla"""

livro = (("Hello","Afonso",2023,),("World","Rafael",2015,),\
         ("Ola","Ana", 2022,),("Mundo","Carol", 2022,),\
            ("Planeta","Jose",2023,),)

print("-".join(str(valor) for valor in livro[3]))

print(sum(1 for valor in livro if valor[1] == "Afonso"))

print(f"-".join(valor[0] for valor in livro))

livro_hello = [v for v in livro if v[0] == "Hello"][0]
print("-".join(map(str, livro_hello)))
saida = "----".join("-".join(map(str, item)) for item in livro)
print(saida)