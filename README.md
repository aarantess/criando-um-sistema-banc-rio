# criando-um-sistema-bancario
# Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python como parte de um desafio para a criação de um sistema com as funcionalidades básicas de um banco: depósito, saque e extrato. Este projeto foi pensado para ser uma versão inicial que pode ser expandida no futuro.

## Funcionalidades

- **Depósito**: Permite depositar valores positivos na conta.
- **Saque**: Limite de 3 saques diários, com um limite máximo de R$ 500,00 por saque. O sistema verifica o saldo antes de autorizar a transação.
- **Extrato**: Exibe todas as movimentações (depósitos e saques) e o saldo atual da conta. Caso não haja movimentações, o sistema exibe uma mensagem informando que nenhuma transação foi realizada.

## Regras de Negócio

- O usuário pode realizar até **3 saques diários**, com um **limite máximo de R$ 500,00** por saque.
- Não é permitido sacar mais do que o saldo disponível na conta.
- O extrato exibe todas as transações realizadas, e se nenhuma transação for realizada, é exibida a mensagem "Não foram realizadas movimentações".
