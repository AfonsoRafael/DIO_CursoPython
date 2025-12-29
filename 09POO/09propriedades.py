class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = nova_idade

# Exemplo de uso
pessoa = Pessoa("Alice", 30)
print(pessoa.nome)  # Acessa o nome usando o getter
pessoa.nome = "Bob" # Define um novo nome usando o setter
print(pessoa.nome)  # Acessa o nome atualizado usando o getter
print(pessoa.idade) # Acessa a idade usando o getter
pessoa.idade = 35   # Define uma nova idade usando o setter
print(pessoa.idade) # Acessa a idade atualizada usando o getter