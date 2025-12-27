# Recursos Públicos e Privados
# Em Python, os atributos e métodos de uma classe são públicos por padrão, o que significa que eles podem ser acessados de fora da classe. No entanto, é possível indicar que um atributo ou método é privado, utilizando um prefixo de dois underscores (__).
# Isso não torna o atributo ou método completamente inacessível, mas sim "name mangling", o que dificulta o acesso direto a ele de fora da classe.
# A convenção de usar dois underscores é uma forma de indicar que o atributo ou método não deve ser acessado diretamente, mas sim através de métodos públicos da classe (getters e setters).

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular          # Atributo público
        self.__saldo = saldo_inicial    # Atributo privado, indicado pelo prefixo __

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def obter_saldo(self):
        return self.__saldo
    
# Exemplo de uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
print(f"Saldo atual: R${conta.obter_saldo()}")
# Tentativa de acesso direto ao atributo privado (não recomendado)
# print(conta.__saldo)  # Isso gerará um erro de atributo