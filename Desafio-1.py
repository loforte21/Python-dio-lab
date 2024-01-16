'''
DESCRIÇÃO
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.
'''

menu = '''
[1] Levantar
[2] Depositar 
[3] Extracto
[0] Sair
'''

saldo = 0 
limite = 500
extracto = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  print(" MENU ".center(25, "#"))
  print(menu)
  print("".center(25, "#"))

  escolha = int(input("Escolha uma opcao: "))

  if escolha == 1:

    print(" LEVANTAR ".center(25, "#"))

    if numero_saques < LIMITE_SAQUES:
      valor_saque = float(input("Insira valor: "))
      if valor_saque < limite:
        if valor_saque < saldo:
          saldo -= valor_saque
          numero_saques += 1
          extracto += f"Saque: {valor_saque:.2f} mt\n"
        else:
          print("Saldo insuficiente!")
      else:
        print("Excedeu o limite de saque!")
    else:
      print("Limites diario de saques atingido!")

    print("".center(25, "#"))
  
  elif escolha == 2: 

    print(" DEPOSITAR ".center(25, "#"))

    deposito = float(input("Insira valor a depositar: "))
    if deposito > 0:
      saldo += deposito
      extracto += f"Deposito: {deposito:.2f} mt\n"
    else:
      print("Valor invalido")

    print("".center(25, "#"))

  elif escolha == 3:

    print(" EXTRACTO ".center(25, "#"))

    print(f"Nao tem historico de movimentos" if not extracto else extracto)
    print(f"Saldo: {saldo:.2f} MT") 
    
    print("".center(25, "#"))

  elif escolha == 0:
    break

  else:
    print("Opcao Invalida!")