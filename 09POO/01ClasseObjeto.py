"""
Desafio 01 - Classe e Objeto
Crie uma classe chamada "bicicleta" com cor,modelo ano e valor
O Objeto deve ter métodos para: buzinar, parar e correr
"""
# self representa a própria instância do objeto, uma convenção mas não é obrigado usar esse nome
class Bicicleta:
    def __init__(self, cor, modelo, ano , valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim!!!")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummm...")

#    def __str__(self):
#        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano} e {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}'for chave,valor in self.__dict__.items()])}"
    #Excelente pois automatiza, se incluir um atributo novo aparecee automaticamente

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor,b1.modelo,b1.ano,b1.valor)

Bicicleta.buzinar(b1)

print(b1) # So aparece formatado por causa do objeto __str__