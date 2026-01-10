# Iteradores em Python
# Um iterador é um objeto que permite percorrer uma coleção de dados, como listas, tuplas ou dicionários, sem expor a estrutura interna da coleção.
# Iteradores implementam dois métodos principais: __iter__() e __next__().
# __iter__() retorna o próprio iterador e __next__() retorna o próximo valor da coleção.
# stopiteration é uma exceção que indica o fim da iteração. importante para controlar loops. quando não há mais itens para retornar, o método __next__() levanta essa exceção para sinalizar o fim da iteração.
 
print("-----------------------------------------------")
print("Exemplo 1: Criando um iterador personalizado")
class meuIterador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.limite:
            valor = self.contador
            self.contador += 1
            return valor
        else:
            raise StopIteration
        
for numero in meuIterador(5):
    print(numero)