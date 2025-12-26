# Herança em POO (Programação Orientada a Objetos)
# A herança é um dos pilares da POO que permite criar uma nova classe baseada em uma classe existente.
# A classe existente é chamada de "classe base" ou "superclasse", e a nova classe é chamada de "classe derivada" ou "subclasse".
# A subclasse herda atributos e métodos da superclasse, podendo também adicionar novos atributos e métodos ou modificar os existentes.
# Benefícios da herança:
# - Representa o mundo real, onde objetos podem ser categorizados em hierarquias.
# - Reutilização de código, evitando duplicação.
# - Facilita a manutenção e a extensão do código.

# Herança Simples e multipla
# Herança Simples: Uma subclasse herda de uma única superclasse.
# Herança Múltipla: Uma subclasse herda de múltiplas superclasses, não suportada em todas as linguagens de programação.
# Exemplo de Herança Simples
class Animal:
    def fazer_som(self):
        return "Som genérico de animal"
    
class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miado"
    

