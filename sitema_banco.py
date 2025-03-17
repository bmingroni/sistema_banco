
# OPERAÇÕES DE BANCO - DEPÓSITO, SAQUE, EXTRATO

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """


saldo = 0
limite = 500
extrato = ''
numeroSaques = 0
LIMITE_SAQUES = 3


while True:
  opcao = input(menu).lower()

  if opcao == 'd':
    print("Operação de depósito selecionada.")
    valor = float(input('Informe o valor do deposito: '))

    if valor > 0:
      saldo += valor
      extrato += f'Depósito: R$ {valor:.2f}\n'
      print(f'Depósito de R${valor:.2f} efetuado com sucesso!')

    else:
      print('A operação falhou! O vamor informado é inválido.')



  elif opcao == 's':
    print("Operação Saque selecionada.")
    valor = float(input('Digite o valor para sacar: '))

    exedeuSaldo = valor > saldo
    exedeuLimite = valor > limite
    exedeuSaques = numeroSaques >= LIMITE_SAQUES

    if exedeuSaldo:
      print('A operação falhou! Você não tem saldo o suficiente.')
    elif exedeuLimite:
      print("A operação falhou! O valor do saque excede o limite.")
    elif exedeuSaques:
         print("Operação falhou! Número máximo de saques excedido.")


    elif valor > 0:
      saldo -= valor
      extrato += f'Saque: R$ {valor:.2f}\n'
      print(f'Saque de R${valor:.2f} efetuado com sucesso!')
      numeroSaques += 1
    else:
      print("Operação falhou! O valor informado é inválido.")



  elif opcao == 'e':
      print('\n================ EXTRATO ================')
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print('==========================================')



  elif opcao == 'q':
    print("Saindo do sistema...")
    break

  else:
      print("Opção inválida! Tente novamente.")