menu = """

    [s] - Sacar
    [d] - Depositar
    [e] - Extrato
    [q] = Sair
    
    => """

saldo = 0.0
saque_diario = 1
saque = 0.0
deposito = 0.0
LIMITE_SAQUE = 3

while True:
    
    print(menu)
    opcao = input("Digite sua operação: ")

    # Opção de saque
    if opcao == "s":
        if saque_diario <= LIMITE_SAQUE:
            valor_saque = float(input("\nDigite o valor a ser sacado: "))
            # Verifica se há saldo para sacar
            if  valor_saque <= saldo:
                if valor_saque > 0 and valor_saque <= 500.00:
                    print("Sacou.")
                    saque += valor_saque
                    saldo -= valor_saque
                    saque_diario += 1
                    print(f"Saldo atual: R${saldo:.2f}")
                else:
                    print("Valor de saque inválido! O valor de saque deve ser no máximo de R$ 500,00.")
            else:
                print("Sem saldo na conta!")
        else:
            print("Já estourou limite de saque!")

    #Opcão de deposito
    elif opcao == "d":
        deposito_valor = float(input("Digite o valor para deposito: "))

        if deposito_valor > 0:
            print(f"Valor depositado: {deposito_valor: .2f}")
            deposito += deposito_valor
            saldo += deposito_valor
        else:
            print("Valor de deposito inválido!")

    # Opção de extrato
    elif opcao == "e":
        print("\nExtrato de sua conta.\n")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"Deposito realizado: R${deposito: .2f}")
        print(f"Valor sacada da conta: R${saque: .2f}")

    # Sair do menu
    elif opcao == "q":
        print("Finalizando operação")
        break

    else:
        print("Opção invalida!")

SystemExit(0)

