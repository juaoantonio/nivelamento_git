from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR')

saldo = 0
extratos = []



while True:
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extratos.append({
                "tipo": "Deposito",
                "valor": valor_deposito,
                "horario": datetime.now().strftime('%H:%M:%S'),
                "data": datetime.now().strftime('%Y-%m-%d')
            })
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= saldo:
            saldo -= valor_saque
            extratos.append({
                "tipo": "Saque",
                "valor": valor_saque,
                "horario": datetime.now().strftime('%H:%M:%S'),
                "data": datetime.now().strftime('%Y-%m-%d')
            })
        else:
            print(f'seu saque no valor de {valor_saque} foi aprovado')
        
        # -----------------------------------------
        # Desenvolva a lógica da validação do saque
        # -----------------------------------------

    elif opcao == '3':
        print(f'\nExtrato bancário:')
        for extrato in extratos:
            print()
            print("-" * 20)
            print(extrato['tipo'])
            print(extrato["valor"])
            print(extrato["horario"])
            print(extrato["data"])
            print("-" * 20)
            print()

        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
