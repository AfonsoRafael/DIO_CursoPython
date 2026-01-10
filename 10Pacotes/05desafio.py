# =========================
# IMPORTAÇÕES
# =========================

# Usado para formatar textos grandes no terminal
import textwrap

# Usado para criar classes abstratas (interfaces)
from abc import ABC, abstractmethod

# Usado para trabalhar com datas e horas
from datetime import datetime


# =========================
# ITERADOR DE CONTAS
# Permite percorrer contas com "for conta in contas"
# =========================
class ContaIterador:
    def __init__(self, contas):
        # Lista de contas que será percorrida
        self.contas = contas
        # Índice interno do iterador
        self.index = 0

    def __iter__(self):
        # Retorna o próprio objeto como iterador
        return self

    def __next__(self):
        # Se o índice passar do tamanho da lista, encerra a iteração
        if self.index >= len(self.contas):
            raise StopIteration

        # Retorna a conta atual
        conta = self.contas[self.index]
        self.index += 1
        return conta


# =========================
# CLASSE CLIENTE (BASE)
# =========================
class Cliente:
    def __init__(self, endereco):
        # Endereço do cliente
        self.endereco = endereco
        # Lista de contas associadas ao cliente
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # Regra de negócio: máximo de 10 transações por dia
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n@@@ Limite diário de transações excedido @@@")
            return

        # Registra a transação na conta
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Associa uma conta ao cliente
        self.contas.append(conta)


# =========================
# CLIENTE PESSOA FÍSICA
# =========================
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe pai
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# =========================
# CLASSE CONTA (BASE)
# =========================
class Conta:
    def __init__(self, numero, cliente):
        # Saldo inicial
        self._saldo = 0
        # Número da conta
        self._numero = numero
        # Agência fixa
        self._agencia = "0001"
        # Cliente dono da conta
        self._cliente = cliente
        # Histórico de transações
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Factory Method para criar contas
        return cls(numero, cliente)

    # Propriedades para acesso seguro aos atributos
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

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
        # Verifica saldo
        if valor > self._saldo:
            print("\n@@@ Saldo insuficiente @@@")
            return False

        # Verifica valor válido
        if valor <= 0:
            print("\n@@@ Valor inválido @@@")
            return False

        # Realiza o saque
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso ===")
        return True

    def depositar(self, valor):
        # Verifica valor válido
        if valor <= 0:
            print("\n@@@ Valor inválido @@@")
            return False

        # Realiza o depósito
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso ===")
        return True


# =========================
# CONTA CORRENTE
# =========================
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        # Filtra os saques feitos hoje
        saques_hoje = [
            t for t in self.historico.transacoes_do_dia()
            if t["tipo"] == Saque.__name__
        ]

        # Regras específicas da conta corrente
        if valor > self._limite:
            print("\n@@@ Valor excede o limite de saque @@@")
            return False

        if len(saques_hoje) >= self._limite_saques:
            print("\n@@@ Limite diário de saques excedido @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        # Representação amigável da conta
        return f"""
Agência:\t{self.agencia}
Conta:\t\t{self.numero}
Titular:\t{self.cliente.nome}
"""


# =========================
# HISTÓRICO DE TRANSAÇÕES
# =========================
class Historico:
    def __init__(self):
        # Lista de transações realizadas
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Registra a transação com data e tipo
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

    def gerar_relatorio(self, tipo=None):
        # Generator para percorrer transações
        for transacao in self._transacoes:
            if tipo is None or transacao["tipo"] == tipo:
                yield transacao

    def transacoes_do_dia(self):
        # Retorna apenas transações do dia atual
        hoje = datetime.now().date()
        return [
            t for t in self._transacoes
            if datetime.strptime(t["data"], "%d-%m-%Y %H:%M:%S").date() == hoje
        ]


# =========================
# TRANSAÇÃO (CLASSE ABSTRATA)
# =========================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


# =========================
# SAQUE
# =========================
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


# =========================
# DEPÓSITO
# =========================
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# =========================
# DECORATOR DE LOG
# =========================
def log_transacao(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# =========================
# MENU
# =========================
def menu():
    texto = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo cliente
[q] Sair
=> """
    return input(textwrap.dedent(texto))


# =========================
# FUNÇÕES AUXILIARES
# =========================
def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta @@@")
        return None
    return cliente.contas[0]


# =========================
# OPERAÇÕES
# =========================
@log_transacao
def depositar(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return

    valor = float(input("Valor do depósito: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Deposito(valor))


@log_transacao
def sacar(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return

    valor = float(input("Valor do saque: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))


@log_transacao
def exibir_extrato(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n=========== EXTRATO ===========")
    extrato = ""
    for t in conta.historico.gerar_relatorio():
        extrato += f"\n{t['data']} - {t['tipo']} - R$ {t['valor']:.2f}"

    print(extrato if extrato else "Sem movimentações")
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("===============================")


# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            nascimento = input("Nascimento: ")
            endereco = input("Endereço: ")
            clientes.append(PessoaFisica(nome, nascimento, cpf, endereco))
            print("Cliente criado com sucesso")

        elif opcao == "nc":
            cpf = input("CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente:
                conta = ContaCorrente.nova_conta(cliente, len(contas) + 1)
                contas.append(conta)
                cliente.adicionar_conta(conta)
                print("Conta criada com sucesso")

        elif opcao == "lc":
            for conta in ContaIterador(contas):
                print(conta)

        elif opcao == "q":
            break

        else:
            print("Opção inválida")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
