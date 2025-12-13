# Os dicionarios em Python são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis, o que significa que podem ser alterados após a criação.
# As chaves devem ser únicas e imutáveis (como strings, números ou tuplas), enquanto os valores podem ser de qualquer tipo de dado.
# Criando um dicionário vazio
dicionario_vazio = {}
# Criando um dicionário com alguns pares chave-valor
dicionario = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}   
# Criando um dicionário usando o construtor dict()
dicionario2 = dict(nome="Bob", idade=25, cidade="Rio de Janeiro")

# Acessando valores no dicionário usando chaves
nome = dicionario["nome"]
idade = dicionario.get("idade")  # Usando o método get()
print("Nome:", nome)
print("Idade:", idade)
# Adicionando um novo par chave-valor
dicionario["profissão"] = "Engenheira"
print("Dicionário após adicionar profissão:", dicionario)
# Modificando um valor existente
dicionario["idade"] = 31
print("Dicionário após modificar idade:", dicionario)

# Dicionarios alinhados 
contatos = {
    "afonso@gmail": {"nome": "Afonso", "telefone": "1234-5678"},
    "bruna@gmail": {"nome": "Bruna", "telefone": "8765-4321"},
    "carla@gmail": {"nome": "Carla", "telefone": "5678-1234"}
}
# Acessando dados do dicionário alinhado
telefone_bruna = contatos["bruna@gmail"]["telefone"]
print("Telefone da Bruna:", telefone_bruna)

# Iterando sobre chaves e valores
for chave, valor in contatos.items():
    print(f"{chave}: {valor}")

for chave in contatos:
    print(f"Email: {chave}, Nome: {contatos[chave]['nome']}")