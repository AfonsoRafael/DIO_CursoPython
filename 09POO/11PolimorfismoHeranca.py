# É possivel implementar polimorfismo em conjunto com herança.
# É possivel modificar o comportamento de um método herdado de uma classe pai na classe filha. É util para adaptar o comportamento de métodos herdados às necessidades específicas da classe filha.
class Passaro:
    def voar(self):
        print("O passaro esta voando.")
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("O avestruz nao pode voar.")

class Aviao(Passaro):
    def voar(self):
        print("O aviao esta voando.")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)  # Saída: "O pardal está voando baixo."
plano_de_voo(p2)  # Saída: "O avestruz não pode voar."
plano_de_voo(Aviao())  # Saída: "O avião está voando alto."