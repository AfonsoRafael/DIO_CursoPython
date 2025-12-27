class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"Animal {self.__class__.__name__} com {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])} "
        
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, ** kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, ** kwargs): # Usando kwargs para repassar os argumentos forma genéricos
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    def fazer_som(self):
        return "Latido"
    
class Gato(Mamifero):
    pass

class Leao(Mamifero):
    def fazer_som(self):
        return "Rugido"
    
class Ornitorinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, n_patas):
        print(Ornitorinco.__mro__) # Mostra a ordem de resolução de métodos (Method Resolution Order)
        # Ordem de precedência: Ornitorinco -> Mamifero -> Ave -> Animal -> object
#        print(Ornitorinco.mro()) # Mostra a ordem de resolução de métodos (Method Resolution Order) Outra forma de ver
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, n_patas=n_patas)
    
gato = Gato(n_patas=4, cor_pelo="Cinza")
print(gato)

ornitorinco = Ornitorinco(n_patas=4, cor_pelo="Marrom", cor_bico="Amarelo")
print(ornitorinco)