# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface Transacao (classe abstrata)
class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("O método registrar deve ser implementado")

# Classe Deposito (implementa Transacao)
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

# Classe Saque (implementa Transacao)
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        if self.valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        if self.valor > conta._saldo:
            print("Operação falhou! Saldo insuficiente.")
            return False
        conta._saldo -= self.valor
        conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")
        return True

# Classe Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
    
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, "0001", cliente)
    
    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)
    
    def depositar(self, valor):
        deposito = Deposito(valor)
        return deposito.registrar(self)

# Classe ContaCorrente (herda de Conta)
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica (herda de Cliente)
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
