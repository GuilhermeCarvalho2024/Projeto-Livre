from banco.usuario import Usuario
from banco.endereco import Endereco 

class Conta(Usuario):
    def __init__(self, nome, cpf, senha, endereco, saldo=0):
        super().__init__(nome, cpf, senha, endereco)
        self.__saldo = saldo  

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def depositar2(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def sacar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, outra_conta, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            outra_conta.depositar2(valor)
            print(f"Transferência de R${valor:.2f} realizada para {outra_conta.nome}.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def to_dict(self):
        return {
            **super().to_dict(),
            'saldo': self.__saldo
        }

    @staticmethod
    def from_dict(data):
        endereco = Endereco.from_dict(data['endereco']) 
        return Conta(data['nome'], data['cpf'], data['senha'], endereco, data['saldo'])