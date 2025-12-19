def menu():
    return """
    ====== Sistema Bancário ======
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Criar Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Sair
    ==============================        
    """
    return input("Escolha uma opção: ")

def depositar(conta,valor,extrato,/):
    """Realiza depósito na conta."""
    if valor > 0:
        conta["saldo"] += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")
    
def sacar(*,conta,valor,extrato,limite_saque,numero_saques,limite_saques):
    """Realiza saque seguindo as regras da conta."""
    if valor > conta["saldo"]:
        print("Saldo insuficiente para saque.")
    elif valor > limite_saque:
        print(f"O valor excede o limite de saque de R$ {limite_saque:.2f}.")
    elif numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        conta["saldo"] -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return numero_saques



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "2":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite =limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por usar nosso sistema bancário.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()