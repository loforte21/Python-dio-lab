'''
DESCRIÇÃO
Neste desafio iremos atualizar a implementação do sistema bancário, 
para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. 
O código deve seguir o modelo de classes UML.
'''

from abc import ABC, abstractmethod, abstractproperty

class Cliente:

  def __init__(self, _endereco):
    self._endereco = _endereco
    self._contas = []
  
  def adicionar_conta(self, conta):
    self._contas.append(conta)
  
  def realizar_tranzacao(self, conta, Transacao):
    Transacao.registrar(conta)     

class Pessoa_fisica(Cliente):

  def __init__(self, cpf, nome, data_nascimento, endereco):
    self.cpf = cpf
    self.nome = nome
    self.data_naccimento = data_nascimento
    super().__init(endereco) 

class Conta:
  
  def __init__(self, numero, cliente):
    self._saldo = 0.00
    self._numero = numero
    self._agencia = "BCI"
    self._cliente = cliente
    self._historico = Historico()

  @property
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def Historico(self):
    return self._historico

  @classmethod
  def nova_conta(cls, cliente, numero):
    return cls(cliente, numero)

  def sacar(self, valor):
    
    if valor > self.saldo:
      print("Operacao Falhou! Saldo Insuficiente.")
      return False
    else:
      self.saldo -= valor
      print("Saque realizado!")
      return True 

  def deposito(self, valor):
    
    if valor > 0:
      print("Deposito realizado!")
      self.saldo += valor
      return True
    else:
      print("Operacao falhou! Valor Invalido")
      return False

class Conta_corrente(Conta):
  
  def __init__(self, numero, cliente):
    super().__init__(numero, cliente)
    self.limite = 500.00
    self.limite_saques = 3

    def sacar(self, valor):

      exceder_saques = numero_saques >= self.limite_saques
      exceder_valor = valor > saldo
      exceder_limite = valor> self.limite

      if exceder_saques:
        print("Falhou: Limite de saques diario excedido!")
      elif exceder_valor:
        print("Falhou: Saldo Insuficiente")
      elif exceder_limite:
        print("Falhou: Valou de saque excedeu limite")
      else:
        if valor> 0:
          saldo -= valor
          numero_saques += 1
          print("SUcesso")

  def depositar(self, valor):
    super().depositar(valor)

class Historico:
  
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes

  def adicionar_transacao(self, transacao):
    self.transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor
      }
    )

class Transacao(ABC):
  
  @property
  @abstractproperty
  def valor(self):
    pass

  @abstractmethod
  def registrar(self, conta):
    pass

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
  
  def registar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

class Saque(Transacao):

  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
  
  def registar(self, conta):
    sucesso_transacao = conta.sacar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)