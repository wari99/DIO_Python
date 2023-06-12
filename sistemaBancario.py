menu = "\n [1]realizar deposito\n [2]fazer saque\n [3]visualizar extrato\n [4]sair\nOperacao desejada: "
extrato = ""

saldo = num_saques = 0
limite = 500
LIM_SAQUES_DIARIOS = 3 

while True:
    num_operacao = input(menu)

    if num_operacao == "1":
        valor = float(input("\nDesejo depositar R$"))
        
        if valor > 0:
            saldo += valor
            extrato += f"DEPOSITOU R${valor:.2f}\n"
        else:
            print("Valor invalido!! ")

    elif num_operacao == "2":

        valor = float(input("\nDesejo sacar R$"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIM_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Limite de saldo excedido!!")
        elif excedeu_limite:
            print("Limite excedido!! ")
        elif excedeu_saques:
            print("Limite de saques diarios excedido!!")
        elif valor > 0:
            saldo -= valor
            extrato += f"SACOU  R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor invalido!!")


    elif num_operacao == "3":
        print("\n*** ** EXTRATO ** ***")
        if(not extrato):
            print("Nao foram realizadas movimentacoes.")
            continue

        print(f"\nSALDO ATUAL: R$ {saldo:.2f} ")
        print("\n*** *** *** ***\n")
        
    elif num_operacao == "4":
        print("\nFim da consulta.")
        break
    
    else:
        print("Operacao invalida!! Disponiveis: [1] [2] [3] ou [4]")
