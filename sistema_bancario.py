menu = """
[d] depósito
[s] saque
[e] extrato
[q] sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Valor do depósito: R$'))
        if valor > limite:
            print('Valor maior que limite permitido.')
            valor = float(input('Valor do depósito: R$'))
        saldo += valor

    elif opcao == 's':

        valor = float(input('Valor do saque: R$'))
        if valor > limite:
            valor = float(input('Valor do saque: R$'))
        if valor > saldo:
            print('saldo indisponível.')
            valor = float(input('Valor do saque: R$'))
        numero_saques += 1
        if numero_saques > LIMITE_SAQUES:
            print('Você atingiu o limite de saques diário.')


    elif opcao == 'e':
        print(f'Seu saldo é de R${saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print('digite um valor válido')