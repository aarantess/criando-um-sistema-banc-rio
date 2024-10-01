# Constantes e variáveis globais
from sistemabancario3 import PessoaFisica


LIMITE_SAQUES = 3
AGENCIA = "0001"
clientes = []
contas = []
numero_conta = 1

# Função para criar um usuário
def criar_usuario(nome, nascimento, cpf, endereco):
    cpf = cpf.replace(".", "").replace("-", "")
    
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            print("Usuário já existente com este CPF!")
            return
    
    cliente = PessoaFisica(cpf, nome, nascimento, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")

# Função para criar uma conta corrente
def criar_conta(cpf):
    global numero_conta
    
    cpf = cpf.replace(".", "").replace("-", "")
    
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            conta = ContaCorrente(numero=numero_conta, agencia=AGENCIA, cliente=cliente, limite=500, limite_saques=LIMITE_SAQUES) # type: ignore
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print(f"Conta {numero_conta} criada com sucesso para o usuário {cliente.nome}!")
            numero_conta += 1
            return
    
    print("Usuário não encontrado! Criação de conta falhou.")

# Função para sacar com o uso da classe Saque
def sacar(cpf, valor):
    conta = selecionar_conta(cpf)
    if conta:
        if conta.sacar(valor):
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação de saque falhou.")

# Função para depositar com o uso da classe Deposito
def depositar(cpf, valor):
    conta = selecionar_conta(cpf)
    if conta:
        if conta.depositar(valor):
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação de depósito falhou.")

# Função para exibir extrato
def exibir_extrato(cpf):
    conta = selecionar_conta(cpf)
    if conta:
        print("\n================ EXTRATO ================")
        if not conta.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in conta.historico.transacoes:
                print(transacao)
        print(f"\nSaldo atual: R$ {conta.saldo():.2f}")
        print("==========================================")

# Função para selecionar uma conta existente com base no CPF
def selecionar_conta(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    for conta in contas:
        if isinstance(conta.cliente, PessoaFisica) and conta.cliente.cpf == cpf:
            return conta
    
    print("Conta não encontrada!")
    return None

# Menu principal
menu = """
================ MENU ================
[u] Criar Usuário
[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """

while True:
    opcao = input(menu).lower()

    if opcao == "u":
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (logradouro, nº, bairro, cidade, estado): ")
        criar_usuario(nome, nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "d":
        cpf = input("Informe o CPF do titular da conta: ")
        valor = float(input("Informe o valor do depósito: "))
        depositar(cpf, valor)

    elif opcao == "s":
        cpf = input("Informe o CPF do titular da conta: ")
        valor = float(input("Informe o valor do saque: "))
        sacar(cpf, valor)

    elif opcao == "e":
        cpf = input("Informe o CPF do titular da conta: ")
        exibir_extrato(cpf)

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma operação válida.")
