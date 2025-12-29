# property() é uma função embutida em Python que permite criar propriedades em classes de forma simples e elegante.
# Propriedades são uma maneira de gerenciar o acesso a atributos de uma classe, permitindo encapsulamento e validação de dados.

class Foo:
    def __init__(self, x = None):
        self._x = x  # Atributo "protegido" (convenção)

    # Getter para a propriedade 'x'
    @property
    def x(self):
        return self._x or 0

    # Setter para a propriedade 'x'
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("O valor de x não pode ser negativo.")
        self._x += value

    # Deleter para a propriedade 'x'
    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)  # Acessa o valor de x usando o getter
foo.x = 20    # Define o valor de x usando o setter
print(foo.x) # Acessa o valor atualizado de x usando o getter
del foo.x      # Remove o atributo x
print(foo.x)  # Acessa o valor de x após o deleter