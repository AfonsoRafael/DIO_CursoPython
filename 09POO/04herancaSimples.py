# Heranca simples em Python
class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print("Motor ligado")

    def __str__(self):
        return f"Veiculo {self.__class__.__name__} {self.cor} com placa {self.placa} e {self.rodas} rodas"
    
class Carro(Veiculo):
    pass
    
class Moto(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carga):# metodo esta sendo sobrescrito, então precisamos chamar o metodo da superclasse
        super().__init__(cor, placa, rodas)
        self.carga = carga
        def carga():
            print(f"Caminhao {'esta carregado' if self.carga else 'não está carregado'}")

# carro.carregado()  Não funciona, pois o método carregado pertence apenas à classe Caminhão

moto = Moto("Vermelha", "XYZ-9876", 2)
print(moto)
moto.ligar_motor()
carro = Carro("Azul", "ABC-1234", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "DEF-5678", 6, True )
caminhao.ligar_motor()
print(caminhao)