# Classes abstratas em Python são definidas usando o módulo `abc` (Abstract Base Classes).
# Uma classe abstrata pode conter métodos abstratos, que são métodos declarados, mas sem implementação.
# Classes que herdam de uma classe abstrata devem implementar todos os métodos abstratos, caso contrário, também serão consideradas abstratas e não poderão ser instanciadas.
# Isso é útil para definir uma interface comum para um conjunto de subclasses, garantindo que todas implementem os mesmos métodos.
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class TV(ControleRemoto):
    def ligar(self): # Implementando o método abstrato, obrigatório para instanciar a classe
        print("TV ligada.")

    def desligar(self):
        print("TV desligada.")

    @property
    def marca(self):
        return "Samsung"

tv = TV()
tv.ligar()    # Saída: TV ligada.
tv.desligar()  # Saída: TV desligada.
print(tv.marca)  # Saída: Samsung