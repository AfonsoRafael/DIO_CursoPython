def menu():
    menu = """
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
    return input(menu)

def depositar(saldo,valor,extrato,/):
    """Realiza depósito na conta."""
    if valor > 0:
        saldo+= valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

    return saldo, extrato
    
def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= limite_saques

    if execedeu_saldo:
        print("Saldo insuficiente.")
    elif execedeu_limite:
        print("Valor do saque excede o limite.")
    elif execedeu_saques:
        print("Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de saque inválido.")
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n======= Extrato =======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, por favor crie um usuário antes de criar uma conta.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        ------------------------------
        """
        print(linha)



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

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por usar nosso sistema bancário.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()