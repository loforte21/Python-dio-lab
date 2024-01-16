'''
DESCRIÇÃO
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.
'''

def menu():
  print(" MENU ".center(25, "#"))
  print("[1] Levantar")
  print("[2] Depositar")
  print("[3] Extracto")
  print("[0] Sair")  
  print("".center(25, "#"))

def main():
  
  saldo = 0 
  limite = 500
  extracto = ""
  numero_saques = 0
  LIMITE_SAQUES = 3

  while True:

    menu()

    escolha = int(input("Escolha uma opcao: "))

    if escolha == 1:
      saldo, extracto, numero_saques = Levantar(saldo=saldo, extracto=extracto, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    
    elif escolha == 2:
      saldo, extracto = depositar(saldo, extracto)

    elif escolha == 3:
      mostrar_extracto(saldo, extracto=extracto)

    elif escolha == 0:
      break

    else:
      print("Opcao Invalida!")


def depositar(saldo, extracto, /):

  print(" DEPOSITAR ".center(25, "#"))

  deposito = float(input("Valor a depositar: "))
  if deposito > 0:
    saldo += deposito
    extracto += f"Deposito: {deposito:.2f} MT\n"
    print("Sucesso")
  else:
    print("Falhou: Valor Invalido!") 

  print("".center(25, "#"), "\n")

  return saldo, extracto

def Levantar(*, saldo, extracto, limite, numero_saques, LIMITE_SAQUES):

  print(" LEVANTAR ".center(25, "#"))

  valor_saque = float(input("Valor a levantar: "))

  exceder_saques = numero_saques >= LIMITE_SAQUES
  exceder_valor = valor_saque > saldo
  exceder_limite = valor_saque > limite

  if exceder_saques:
    print("Falhou: Limite de saques diario excedido!")
  elif exceder_valor:
    print("Falhou: Saldo Insuficiente")
  elif exceder_limite:
    print("Falhou: Valou de saque excedeu limite")
  else:
    if valor_saque > 0:
      saldo -= valor_saque
      numero_saques += 1
      extracto += f"Saque: {valor_saque:.2f} MT\n"
      print("SUcesso")

  print("".center(25, "#"), "\n")

  return saldo, extracto, numero_saques

def mostrar_extracto(saldo, / , *, extracto):

  print(" EXTRACTO ".center(25, "#"))

  print(extracto if extracto else "Nenhuma operacao realizada")
  print(f"Saldo: {saldo:.2f} MT")

  print("".center(25, "#"), "\n")

main()