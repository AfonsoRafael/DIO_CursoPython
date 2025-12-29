# Variaveis de Instancia
# Variaveis de instancia sao aquelas que sao declaradas dentro do metodo construtor __init de uma classe. Cada objeto (instancia) da classe possui suas proprias copias dessas variaveis, permitindo que cada objeto mantenha seu proprio estado.

class Estudante:
    escola = "DIO"  # Variavel de classe
    def __init__(self, nome, idade):
        self.nome = nome          # Variavel de instancia
        self.idade = idade        # Variavel de instancia

    def __str__(self):
        return f"Meu nome e {self.nome} e tenho {self.idade} anos, e estudo na escola {self.escola}."
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
estudante1 = Estudante("Joao", 20)
estudante2 = Estudante("Maria", 22)
print(estudante1)  # Saída: Meu nome é Joao e tenho 20 anos, e estudo na escola DIO.
print(estudante2)  # Saída: Meu nome é Maria e tenho 22 anos, e estudo na escola DIO.

# Ou seja cada objeto (estudante1 e estudante2) tem suas proprias variaveis de instancia (nome e idade), enquanto a variavel de classe (escola) é compartilhada entre todas as instancias da classe Estudante, sendo unico.

mostrar_valores(estudante1, estudante2)
# Podemos modificar os valores das variaveis de instancia de cada objeto individualmente, sem afetar os outros objetos.
estudante1.nome = "Carlos"
estudante1.idade = 21
print(estudante1)  # Saída: Meu nome é Carlos e tenho 21 anos, e estudo na escola DIO.
mostrar_valores(estudante1, estudante2)
# A variavel de classe permanece inalterada para todas as instancias.
Estudante.escola = "DIO - Digital Innovation One"
mostrar_valores(estudante1, estudante2)
# Agora a variavel de classe foi alterada para todas as instancias da classe Estudante.