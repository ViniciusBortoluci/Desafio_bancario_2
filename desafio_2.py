def menu_op():
    menu = """
    Selecione a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Cliente
    [5] Criar Conta     
    [6] Listar Clientes
    [7] Limite de saques
    [0] Sair

    - """
    return input(menu)


def depositar(saldo, extrato):
    while True:
        try:
            deposito = float(input("Informe o valor que será depositado: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
                return saldo, extrato
            else:
                print(
                    "Operação falhou! O valor informado é inválido. Digite um valor positivo.")
        except ValueError:
            print("Operação falhou! Entrada inválida. Por favor, digite um número.")


def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    while True:
        try:
            valor_saque = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(
                    f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print(
                    f"Operação falhou! Você atingiu o número máximo de {limite_saques} saques permitidos.")
            elif valor_saque <= 0:
                print(
                    "Operação falhou! O valor informado é inválido. Digite um valor positivo.")
            else:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                return saldo, extrato, numero_saques
        except ValueError:
            print("Operação falhou! Entrada inválida. Por favor, digite um número.")
        # Retorno em caso de erro na entrada inicial
        return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n---------- EXTRATO ----------")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("----------------------------")


def verificar_saques(numero_saques, limite_saques):
    print(f"\nNúmero de saques efetuados: {numero_saques}")
    print(f"Número máximo de saques permitidos: {limite_saques}")


def cadastrar_cliente(clientes):
    print("\n---------- CADASTRO DE NOVO CLIENTE ----------")
    cpf = int(input("Informe o CPF (somente números): "))

    # Verifica se o CPF já existe
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Operação falhou! Já existe um cliente cadastrado com este CPF.")
            return clientes  # Retorna a lista de clientes sem alterações

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    return clientes  # Retorna a lista de clientes atualizada


def listar_clientes(clientes):
    print("\n---------- CLIENTES CADASTRADOS ----------")
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        for i, cliente in enumerate(clientes):
            print(f"\nCliente {i+1}:")
            print(f"  Nome: {cliente['nome']}")
            print(f"  CPF: {cliente['cpf']}")
            print(f"  Data de Nascimento: {cliente['data_nascimento']}")
            print(f"  Endereço: {cliente['endereco']}")
            print("------------------------------------------")


def criar_conta(contas, clientes, proximo_numero_conta):
    print("\n---------- CRIAR NOVA CONTA ----------")
    cpf_cliente = int(
        input("Informe o CPF do cliente para vincular a conta: "))

    # Busca o cliente pelo CPF
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["cpf"] == cpf_cliente:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado! Cadastre o cliente primeiro.")
        return contas, proximo_numero_conta

  
    numero_agencia = "0001"
    nova_conta = {
        "agencia": numero_agencia,
        "numero_conta": proximo_numero_conta,
        "cpf_cliente": cpf_cliente,
        "saldo": 0,
        "extrato": "",
        "numero_saques_hoje": 0
    }

    contas.append(nova_conta)
    print(
        f"Conta criada com sucesso! Agência: {numero_agencia}, Conta: {proximo_numero_conta}")
    return contas, proximo_numero_conta + 1


def main():

    clientes = []
    contas = []  
    proximo_numero_conta = 1  # Contador para o número sequencial das contas

    saldo = 0
    limite = 500
    extrato = ""

    LIMITE_SAQUES = 3
    numero_saques = 0

    while True:
        opcao = menu_op()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            clientes = cadastrar_cliente(clientes)
        elif opcao == "5":  # Nova opção para criar conta
            contas, proximo_numero_conta = criar_conta(
            contas, clientes, proximo_numero_conta)
        elif opcao == "6":
            listar_clientes(clientes)
        elif opcao == "7":
            verificar_saques(numero_saques, LIMITE_SAQUES)
        elif opcao == "0":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, selecione uma opção válida do menu.")


# Chama a função principal para iniciar o programa
main()
