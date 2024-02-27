from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR')

saldo = 0
extratos = []

def registro_extrato (tipo, valor):
    extratos.append({
                "tipo": tipo,
                "valor": valor,
                "horario": datetime.now().strftime('%H:%M:%S'),
                "data": datetime.now().strftime('%Y-%m-%d')
            })

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
            registro_extrato("Depósito", valor_deposito)
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque < 0:
            print('\nNão é possivel sacar um número negativo.')
        elif valor_saque <= saldo:
            print(f'\nSaque de R${valor_saque} realizado com sucesso.')
            saldo -= valor_saque
            registro_extrato('Saque', valor_saque)
        else: 
          print('\nNão é possivel realizar um saque de valor maior que o saldo.')

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
