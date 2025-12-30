class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nasc(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_data_nasc(1990, 5, 15, "Ana")
print(f"Nome: {p.nome}, Idade: {p.idade}")  # Saída: Nome: Ana, Idade: 35
print(Pessoa.maior_de_idade(p.idade))  # Saída: True
print(Pessoa.maior_de_idade(16))  # Saída: False