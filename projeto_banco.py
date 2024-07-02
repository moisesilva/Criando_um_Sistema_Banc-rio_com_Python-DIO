menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
        else:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor > limite:
                print(f"Valor excede o limite de saque de R$ {limite:.2f} por operação.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque realizado: R$ {valor:.2f}")
            else:
                print("Valor inválido para saque.")
    
    elif opcao == "e":
        print("\nExtrato:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
    
    elif opcao == "q":
        print("Sair")
        break
    
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
