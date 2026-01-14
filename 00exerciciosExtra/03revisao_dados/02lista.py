# Escreva um programa que recebe uma lista de nomes do usuário (até que ele digite "sair") e:

# Ordene os nomes em ordem alfabética

# Conte quantos nomes começam com a letra "A"

# Remova nomes duplicados (mantendo apenas uma ocorrência)

nomes = []
while True:
    
    nome = input("Digite um nome, se desejar sair, digite sair: ").strip().title()
    if nome == "Sair":
        break
    nomes.append(nome)

nomes.sort()
print("-".join(nomes))
cont = 0
for nome in nomes:
    if nome[0] == "A":
        cont+=1
    
print(f"A quantidade de nomes que começam com 'a' e {cont}")

for nome in nomes:
    if nomes.count(nome.title()) > 1:
        nomes.remove(nome)

print("-".join(nomes))