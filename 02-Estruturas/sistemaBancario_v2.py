def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n** Depósito realizado com sucesso! **")
    else:
        print("\nValor invalido!!")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n** Saldo insuficiente!! **")

    elif excedeu_limite:
        print("\n** Limite excedido!! **")

    elif excedeu_saques:
        print("\n** Numero de saques diarios excedido!! **")

    elif valor > 0:
        saldo -= valor
        extrato += f"Desejo sacar R${valor:.2f}\n"
        numero_saques += 1
        print("\n** Saque realizado!! **")

    else:
        print("\nValor invalido!!")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n*** **  EXTRATO *** ** ")
    if(not extrato): 
        print("Nao foram realizadas movimentacoes.")
    print(f"\nSALDO: R${saldo:.2f}")
    print("*** ** *** ** *** ** *** **")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJa existe um usuario com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("* ** Usuário criado com sucesso! ** *")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n** Conta criada com sucesso! **")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n** Usuário não encontrado, fluxo de criação de conta encerrado! **")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("*" *50)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        menu = """
[d]  realizar deposito
[s]  fazer saque
[e]  visualizar extrato
[nc] nova conta
[lc] listar contas
[nu] criar novo usuario
[q]  sair
    Operacao: """
        
        num_operacao = input(menu)

        if num_operacao == "d":
            valor = float(input("Valor do deposito: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif num_operacao == "s":
            valor = float(input("Valor a sacar: R$"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif num_operacao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif num_operacao == "nu":
            criar_usuario(usuarios)

        elif num_operacao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif num_operacao == "lc":
            listar_contas(contas)

        elif num_operacao == "q":
            break

        else:
            print("Operacao invalida!! Selecione novamente.")

main()
