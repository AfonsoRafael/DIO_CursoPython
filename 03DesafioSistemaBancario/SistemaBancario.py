# Dicionário representando a conta bancária
conta = {
    "saldo": 0.0,
    "extrato": [],
    "limite_saque": 500.0,
    "numero_saques": 0,
    "limite_saques": 3
}


def depositar(conta, valor):
    """Realiza depósito na conta."""
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")


def sacar(conta, valor):
    """Realiza saque seguindo as regras da conta."""
    if valor > conta["saldo"]:
        print("Saldo insuficiente para saque.")
    elif valor > conta["limite_saque"]:
        print(f"O valor excede o limite de saque de R$ {conta['limite_saque']:.2f}.")
    elif conta["numero_saques"] >= conta["limite_saques"]:
        print("Limite diário de saques atingido.")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")


def exibir_extrato(conta):
    """Exibe extrato de todas as movimentações da conta."""
    print("\n====== Extrato ======")

    if not conta["extrato"]:
        print("Nenhuma movimentação registrada.")
    else:
        for item in conta["extrato"]:
            print(item)

    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("=====================\n")


# Loop principal do programa
while True:
    menu = """
    ====== Sistema Bancário ======
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair
    ==============================        
    """
    print(menu)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para saque: R$ "))
        sacar(conta, valor)

    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: R$ "))
        depositar(conta, valor)

    elif opcao == "3":
        exibir_extrato(conta)

    elif opcao == "4":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida. Tente novamente.")
