# metodos __init__ e __del__
# __init__ é sempre executado quando uma nova instancia de classe é criada, nesse medoto iniciamos o estado do objeto - metodo inicializador

# __del__ metodo destrutor é executado quando uma instancia é destruida, não sao tao necessarios em python pois ele tem um coletor de lixo que lida com o gerenciamento de memoria automaticamente - em C++ é mais util

class cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordade = acordado

    def falar(self):
        print("Auau")

    def __del__(self):
        print(f"Removendo a instancia da classe {self.nome}")

def cria_cao():
        c2 = cachorro("Irineu", "Preto", False)
        print(c2.nome)

c = cachorro("Toto","Branco")
c.falar()

cria_cao()
print("Ola mundo")
print("Ola mundo")
del c #Normalmente destroi no final mas isso força antes
print("Ola mundo")
print("Ola mundo")