# 📘 Sistema Bancário em Python

Este projeto implementa um sistema bancário simples utilizando Python, com foco em organização, boas práticas e separação de responsabilidades.  
A aplicação permite **depósitos, saques e exibição de extrato**, utilizando um **dicionário para armazenar os dados da conta**, evitando variáveis globais e tornando o código mais limpo e fácil de manter.

---

## Funcionalidades

- **Depósito**  
  Permite adicionar valores ao saldo e registra a operação no extrato.

- **Saque**  
  Aplicam-se regras de segurança:
  - Limite de R$ 500 por saque  
  - Limite de 3 saques por dia  
  - Validação de saldo disponível  

- **Extrato**  
  Lista todas as operações realizadas (saques e depósitos), além do saldo atual.

- **Menu interativo**  
  O usuário navega pelas opções do sistema até escolher sair.

---

## Estrutura da Conta

A conta é representada com um dicionário:

```python
conta = {
    "saldo": 0.0,
    "extrato": [],
    "limite_saque": 500.0,
    "numero_saques": 0,
    "limite_saques": 3
}
