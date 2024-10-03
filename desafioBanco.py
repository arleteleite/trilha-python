#Refatorando o código do banco
#Implemantando funções.

# Função para exibir o menu
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [t] Transferir
    [q] Sair

    => """
    return input(menu)

# Função para realizar o depósito
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar o saque
def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Função para realizar a transferência
def transferir(saldo, extrato, numero_transferencia, LIMITE_TRANSFERENCIA, limite):
    valor = float(input("Informe o valor a transferir: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_transferencia = numero_transferencia >= LIMITE_TRANSFERENCIA

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor da transferência excede o limite.")
    elif excedeu_transferencia:
        print("Operação falhou! Número máximo de transferências excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Transferência: R$ {valor:.2f}\n"
        numero_transferencia += 1
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_transferencia

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função principal
def main():
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    numero_transferencia = 0
    LIMITE_SAQUES = 3
    LIMITE_TRANSFERENCIA = 2

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

        elif opcao == "t":
            saldo, extrato, numero_transferencia = transferir(saldo, extrato, numero_transferencia, LIMITE_TRANSFERENCIA, limite)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executa o sistema bancário
main()
