# Constantes e variáveis globais
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []
numero_conta = 1

# Função para criar um usuário
def criar_usuario(nome, nascimento, cpf, endereco):
    cpf = cpf.replace(".", "").replace("-", "")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já existente com este CPF!")
            return
    
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

# Função para criar uma conta corrente
def criar_conta(cpf):
    global numero_conta
    
    cpf = cpf.replace(".", "").replace("-", "")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": "", "numero_saques": 0})
            print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")
            numero_conta += 1
            return
    
    print("Usuário não encontrado! Criação de conta falhou.")

# Função para sacar com argumentos apenas por nome
def sacar(*, conta, valor):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return

    if valor > conta["saldo"]:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > 500:
        print("Operação falhou! O limite por saque é de R$ 500.00.")
    elif conta["numero_saques"] >= LIMITE_SAQUES:
        print(f"Operação falhou! Você atingiu o limite de {LIMITE_SAQUES} saques diários.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Função para depositar com argumentos apenas por posição
def depositar(conta, valor, /):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para exibir extrato com argumentos por posição e nome
def exibir_extrato(conta, /, *, saldo):
    print("\n================ EXTRATO ================")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        print(conta["extrato"])
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Função para selecionar uma conta existente com base no CPF
def selecionar_conta(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
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
        conta = selecionar_conta(cpf)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            depositar(conta, valor)

    elif opcao == "s":
        cpf = input("Informe o CPF do titular da conta: ")
        conta = selecionar_conta(cpf)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            sacar(conta=conta, valor=valor)

    elif opcao == "e":
        cpf = input("Informe o CPF do titular da conta: ")
        conta = selecionar_conta(cpf)
        if conta:
            exibir_extrato(conta, saldo=conta["saldo"])

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma operação válida.")
