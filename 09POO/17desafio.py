from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

# Importação de bibliotecas
# ABC: para criar classes abstratas
# Datetime: para trabalhar com datas
# Textwrap: para formatar texto

class Cliente:
    def __init__(self, endereco):
        # Inicializacao de um cliente com endereco
        self.endereco = endereco
        # Lista para armazenar contas dos clientes
        self.contas = []

    def adicionar_conta(self, conta):
        # Adiciona uma conta a lista de contas do cliente
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        # Delega aexecucao da transacao para o metodo registrar da transacao
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe pai
        super().__init__(endereco)
        # Atributos especificos de pessoa fisica
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf #Identificador unico


class Conta:
    def __init__(self, numero, cliente):
        # Atributos privados
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Metodo de fabrica para criar nova conta
        return cls(numero, cliente) # cls representa a propria classe

    #Propriedades gets, acesso controlado
    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        # Verifica se o valor e positivo
        if valor <= 0:
            print("\nOperacao falhou, valor invalido")
            return False
        # Verifica se o saldo e positivo
        if valor > self.saldo:
            print("\nOperacao falhou, saldo insuficiente")
            return False

        # Subtrai o valor do saldo
        self._saldo -= valor
        print("\nSaque realizado com sucesso")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\nOperacao falhou, valor invalido")
            return False

        # Adciciona o valor no saldo
        self._saldo += valor
        print("\nDeposito realizado com sucesso")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Chama construtor da classe pai
        super().__init__(numero, cliente)
        # Atributos especificos da conta corrente
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite=500, limite_saques=3):
        # Subscreve o metodo com parametros adicionais
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        # Conta quantos saques ja foram feitos
        numero_saques = sum(
            1 for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__
        )

        if valor > self.limite:
            print("\nOperacao falhou, valor do saque excede o limite")
            return False

        if numero_saques >= self.limite_saques:
            print("\nOperacao falhou, numero maximo de saques excedido")
            return False
        # Se todas as validocoes passarem chama o metodo sacar da classe pai
        return super().sacar(valor)

    def __str__(self):
        return f"""\
Agencia:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
"""


class Historico:
    def __init__(self):
    # Lista para armazenar as transacoes
        self._transacoes = []

    @property
    def transacoes(self):
        # Retorna a lista de transacoes
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Adiciona uma transacao ao historico
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC): # Classe abstrata
    @property
    @abstractmethod
    def valor(self):
        # Metodo abstrato que deve ser implementado na classe filha
        pass

    @abstractmethod
    def registrar(self, conta):
        # Metodo abstrato que deve ser implementado na classe filha
        pass


class Saque(Transacao):
    def __init__(self, valor):
        # Retorna o valor do saque
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Executa o saque e registra no historico se bem sucedido
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Executa deposito e registra no historico se bem sucedido
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """\n
=======================================
            BANCO PYTHON
=======================================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova Conta
[5]\tListar Contas
[6]\tNovo Usuario
[0]\tSair
=> """
    # textwrap remove a identacao comum das strings multiplas
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    # Procura um cliente pelo cpf na lista de clientes
    # next(), retorna o primeiro cpf ou None
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)


def recuperar_conta_cliente(cliente):
    # Retorna a primeira conta do cliente ou None
    if not cliente.contas:
        print("\nCliente nao possui conta")
        return None
    return cliente.contas[0] # Apenas a primeira


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    # Busca pelo cpf do cliente
    cliente = filtrar_cliente(cpf, clientes)
    # Se nao encontrar retorna
    if not cliente:
        print("Cliente nao encontrado")
        return
    # Solicita valor
    valor = float(input("Informe o valor do deposito: "))
    # Recupera conta do cliente
    conta = recuperar_conta_cliente(cliente)
    if conta:
        # Executa transacao de deposito
        cliente.realizar_transacao(conta, Deposito(valor))


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente nao encontrado")
        return

    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente nao encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    # Verifica se a transacoes no historico
    if not conta.historico.transacoes:
        print("Nao foram realizadas movimentacoes.")
    else:
        # Itera sobre todas as transacoes e exibe
        for t in conta.historico.transacoes:
            print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")

    # Exibe saldo atual
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("=========================================")


def criar_conta(numero_contas, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente nao encontrado")
        return
    # Cria conta corrente com numero seguencial
    conta = ContaCorrente.nova_conta(cliente, numero_contas)
    # Adiciona a lista geral de contas
    contas.append(conta)
    # Adiciona a lista de contas do cliente
    cliente.adicionar_conta(conta)

    print("Conta criada com sucesso")


def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(textwrap.dedent(str(conta)))


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente numeros): ")
    # Verifica se cpf ja existe
    if filtrar_cliente(cpf, clientes):
        print("Ja existe cliente com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco: ")
    # Cria novo objeto de pessoa fisica
    clientes.append(
        PessoaFisica(nome, data_nascimento, cpf, endereco)
    )

    print("Cliente criado com sucesso")


def main():
    # Lista para armazenar dados na memoria
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)
        elif opcao == "2":
            sacar(clientes)
        elif opcao == "3":
            exibir_extrato(clientes)
        elif opcao == "4":
            # Passa o proximo numero de conta disponivel
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_cliente(clientes)
        elif opcao == "0":
            break
        else:
            print("Operacao invalida")


main()
